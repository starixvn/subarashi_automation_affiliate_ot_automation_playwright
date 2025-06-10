import time
import functools
import traceback
from typing import Any, Callable, Optional, Type, TypeVar, Union, cast, Dict
from datetime import datetime, timedelta
import inspect

from src.utils.core.exceptions import AutomationException
from src.utils.core.logging import get_logger

logger = get_logger(__name__)

F = TypeVar('F', bound=Callable[..., Any])

_test_case_last_checklist = {}

def retry(
    max_attempts: Union[int, Callable[[Any], int]] = 3,
    delay_seconds: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions_to_retry: tuple = (Exception,),
    should_retry: Optional[Union[Callable[[Exception], bool],
                                Callable[[Any, Exception], bool]]] = None,
) -> Callable[[F], F]:
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

def track_last_checklist(original_update_method):
    @functools.wraps(original_update_method)
    def wrapper(self, spread_sheet_id, checklist, auto_testcase, sub_auto_testcases, auto_status, sheet_name="Checklist", duration=None):
        _test_case_last_checklist[auto_testcase] = {
            'spread_sheet_id': spread_sheet_id,
            'checklist': checklist,
            'sheet_name': sheet_name
        }
        return original_update_method(self, spread_sheet_id, checklist, auto_testcase, sub_auto_testcases, auto_status, sheet_name, duration)
    return wrapper

def measure_test_execution_time(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        test_name = func.__name__
        start_time = time.time()
        
        try:
            result = func(self, *args, **kwargs)
            
            end_time = time.time()
            execution_time = end_time - start_time
            
            duration = str(timedelta(seconds=int(execution_time)))
            if '.' in duration:
                duration = duration.split('.')[0]
            
            if test_name in _test_case_last_checklist:
                last_info = _test_case_last_checklist[test_name]
                
                utils = None
                
                if hasattr(self, "utils"):
                    utils = self.utils
                elif hasattr(self, "check_data_referrers") and hasattr(self.check_data_referrers, "utils"):
                    utils = self.check_data_referrers.utils
                elif hasattr(self, "test_class") and hasattr(self.test_class, "utils"):
                    utils = self.test_class.utils
                
                if utils is not None:
                    if hasattr(utils, "update_duration_only"):
                        utils.update_duration_only(
                            last_info['spread_sheet_id'],
                            test_name,
                            duration,
                            last_info['sheet_name']
                        )
                    else:
                        utils.update_result_to_ggsheet(
                            last_info['spread_sheet_id'],
                            last_info['checklist'],
                            test_name,
                            "",
                            "",
                            last_info['sheet_name'],
                            duration
                        )
                else:
                    logger.warning(f"Cannot find utils object to update duration for test '{test_name}'")
            
            return result
        except Exception as e:
            end_time = time.time()
            execution_time = end_time - start_time
            
            duration = str(timedelta(seconds=int(execution_time)))
            if '.' in duration:
                duration = duration.split('.')[0]
            
            try:
                if test_name in _test_case_last_checklist:
                    last_info = _test_case_last_checklist[test_name]
                    
                    utils = None
                    if hasattr(self, "utils"):
                        utils = self.utils
                    elif hasattr(self, "check_data_referrers") and hasattr(self.check_data_referrers, "utils"):
                        utils = self.check_data_referrers.utils
                    elif hasattr(self, "test_class") and hasattr(self.test_class, "utils"):
                        utils = self.test_class.utils
                    
                    if utils is not None:
                        if hasattr(utils, "update_duration_only"):
                            utils.update_duration_only(
                                last_info['spread_sheet_id'],
                                test_name,
                                duration,
                                last_info['sheet_name']
                            )
                        else:
                            utils.update_result_to_ggsheet(
                                last_info['spread_sheet_id'],
                                last_info['checklist'],
                                test_name,
                                "",
                                "",
                                last_info['sheet_name'],
                                duration
                            )
            except Exception as update_error:
                logger.error(f"Failed to update duration for test '{test_name}': {str(update_error)}")
            raise e
            
    return wrapper

