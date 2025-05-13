"""
Decorators module providing utility decorators for the automation framework.
This module contains decorators for retry mechanisms, exception handling,
performance monitoring, and exception type conversion.
"""
import time
import functools
import traceback
from typing import Any, Callable, Optional, Type, TypeVar, Union, cast, Dict

from src.utils.core.exceptions import AutomationException
from src.utils.core.logging import get_logger

logger = get_logger(__name__)

F = TypeVar('F', bound=Callable[..., Any])

def retry(
    max_attempts: Union[int, Callable[[Any], int]] = 3,
    delay_seconds: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions_to_retry: tuple = (Exception,),
    should_retry: Optional[Union[Callable[[Exception], bool],
                                Callable[[Any, Exception], bool]]] = None,
) -> Callable[[F], F]:
    """
    Retry decorator that retries the function if it raises specified exceptions.

    Args:
        max_attempts: Maximum number of attempts to retry or a callable that returns this value
        delay_seconds: Initial delay between retries in seconds
        backoff_factor: Factor by which the delay increases after each retry
        exceptions_to_retry: Tuple of exception types to catch and retry
        should_retry: Optional callable to determine if retry should happen

    Returns:
        Decorated function that implements retry logic
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            is_instance_method = args and hasattr(args[0], func.__name__)
            self_instance = args[0] if is_instance_method else None

            actual_max_attempts = max_attempts
            if callable(max_attempts) and is_instance_method and self_instance is not None:
                actual_max_attempts = max_attempts(self_instance)

            attempt = 1
            current_delay = delay_seconds
            last_exception = None

            func_name = getattr(func, "__qualname__", func.__name__)

            while attempt <= actual_max_attempts:
                try:
                    if attempt > 1:
                        logger.debug("Retry attempt %s/%s for %s",
                                    attempt, actual_max_attempts, func_name)

                    return func(*args, **kwargs)

                except exceptions_to_retry as e:
                    last_exception = e

                    should_retry_this = True
                    if should_retry is not None:
                        if (is_instance_method and self_instance is not None
                                and callable(should_retry)):
                            should_retry_this = should_retry(self_instance, e)
                        elif callable(should_retry):
                            should_retry_this = should_retry(e)

                    if not should_retry_this or attempt == actual_max_attempts:
                        logger.debug(
                            "Not retrying %s after attempt %s/%s. Exception: %s: %s",
                            func_name, attempt, actual_max_attempts,
                            type(e).__name__, str(e)
                        )
                        raise

                    logger.debug(
                        "Retrying %s in %.2fs after exception: %s: %s",
                        func_name, current_delay, type(e).__name__, str(e)
                    )

                    time.sleep(current_delay)

                    current_delay *= backoff_factor
                    attempt += 1

            if last_exception:
                raise last_exception

            return None

        return cast(F, wrapper)

    return decorator

def log_exceptions(
    log_level: str = "ERROR",
    log_traceback: bool = True,
    message_template: str = "Error in {func_name}: {error}",
    re_raise: bool = True,
) -> Callable[[F], F]:
    """
    Decorator to log exceptions raised by a function.

    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_traceback: Whether to include traceback in the log
        message_template: Template string for the log message
        re_raise: Whether to re-raise the exception after logging

    Returns:
        Decorated function that logs exceptions
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except (ValueError, TypeError, KeyError, AttributeError,
                  IndexError, IOError, AutomationException) as e:
                func_name = getattr(func, "__qualname__", func.__name__)

                log_message = message_template.format(func_name=func_name, error=str(e))

                if log_traceback:
                    tb = traceback.format_exc()
                    log_message = f"{log_message}\nTraceback:\n{tb}"

                log_method = getattr(logger, log_level.lower(), logger.error)
                log_method(log_message)

                if re_raise:
                    raise

                return None

        return cast(F, wrapper)

    return decorator

def monitor_performance(
    log_level: str = "DEBUG",
    threshold_seconds: Optional[float] = None,
) -> Callable[[F], F]:
    """
    Decorator to monitor the execution time of a function.

    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        threshold_seconds: Only log if execution time exceeds this threshold

    Returns:
        Decorated function that monitors performance
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = getattr(func, "__qualname__", func.__name__)

            start_time = time.time()

            try:
                result = func(*args, **kwargs)

                execution_time = time.time() - start_time

                if threshold_seconds is None or execution_time >= threshold_seconds:
                    log_method = getattr(logger, log_level.lower(), logger.debug)
                    log_method("%s executed in %.4f seconds", func_name, execution_time)

                return result

            except Exception as e:
                execution_time = time.time() - start_time

                log_method = getattr(logger, log_level.lower(), logger.debug)
                log_method(
                    "%s failed after %.4f seconds with exception: %s: %s",
                    func_name, execution_time, type(e).__name__, str(e)
                )

                raise

        return cast(F, wrapper)

    return decorator

def convert_exceptions(
    exception_map: Dict[Type[Exception], Type[Exception]],
    pass_original: bool = True,
) -> Callable[[F], F]:
    """
    Decorator to convert exceptions to different exception types.

    Args:
        exception_map: Dictionary mapping source exception types to target types
        pass_original: Whether to pass the original exception to the new one

    Returns:
        Decorated function that converts exceptions
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                for source_type, target_type in exception_map.items():
                    if isinstance(e, source_type):
                        func_name = getattr(func, "__qualname__", func.__name__)

                        if pass_original and issubclass(target_type, AutomationException):
                            raise target_type(
                                message=f"Exception in {func_name}: {str(e)}",
                                original_exception=e
                            ) from e

                        raise target_type(f"Exception in {func_name}: {str(e)}") from e

                raise

        return cast(F, wrapper)

    return decorator

