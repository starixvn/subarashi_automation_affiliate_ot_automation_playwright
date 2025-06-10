import os
import json
import time
import random
import string
import platform
import datetime
from pathlib import Path
from typing import Any, Dict, Tuple, Union, TypeVar

from src.utils.core.exceptions import ValidationException, FileException, TimeoutException
from src.utils.core.logging import get_logger

logger = get_logger(__name__)

T = TypeVar('T')

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def generate_unique_id(prefix: str = "", length: int = 8) -> str:
    if length <= 0:
        raise ValidationException(f"ID length must be positive, got {length}")

    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    timestamp = int(time.time())

    if prefix:
        return f"{prefix}_{random_part}_{timestamp}"
    return f"{random_part}_{timestamp}"


def get_timestamp(format_str: str = "%Y%m%d_%H%M%S") -> str:
    return datetime.datetime.now().strftime(format_str)


def pretty_dict(data: Dict) -> str:
    return json.dumps(data, indent=2, sort_keys=True)


def load_json_file(file_path: Union[str, Path]) -> Dict:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as exc:
        raise FileException(f"JSON file not found: {file_path}") from exc
    except json.JSONDecodeError as e:
        raise FileException(f"Invalid JSON in file {file_path}: {str(e)}") from e
    except Exception as e:
        raise FileException(f"Error reading JSON file {file_path}: {str(e)}") from e


def save_json_file(data: Dict, file_path: Union[str, Path], pretty: bool = True) -> None:
    try:
        indent = 2 if pretty else None
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
    except Exception as e:
        raise FileException(f"Error writing JSON file {file_path}: {str(e)}") from e


def ensure_directory_exists(directory_path: Union[str, Path]) -> Path:
    path = Path(directory_path)
    try:
        path.mkdir(parents=True, exist_ok=True)
        return path
    except Exception as e:
        raise FileException(f"Failed to create directory {directory_path}: {str(e)}") from e


def get_environment_info() -> Dict[str, str]:
    return {
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "system": platform.system(),
        "release": platform.release(),
        "node": platform.node(),
        "processor": platform.processor(),
        "cpu_count": str(os.cpu_count()),
        "cwd": os.getcwd(),
        "timestamp": get_timestamp(),
    }


def format_duration(seconds: float) -> str:
    if seconds < 0.001:
        return f"{seconds * 1000000:.2f} μs"
    if seconds < 1:
        return f"{seconds * 1000:.2f} ms"
    if seconds < 60:
        return f"{seconds:.2f} s"

    minutes, remaining_seconds = divmod(seconds, 60)
    return f"{int(minutes)}m {remaining_seconds:.2f}s"


def truncate_string(text: str, max_length: int = 100, suffix: str = "...") -> str:
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def wait_until(condition: callable, timeout: float = 10.0, poll_interval: float = 0.5,
               error_message: str = "Timeout waiting for condition", **kwargs) -> Any:
    start_time = time.time()
    last_exception = None

    while time.time() - start_time < timeout:
        try:
            result = condition(**kwargs)
            if result:
                return result
        except Exception as e:
            last_exception = e

        time.sleep(poll_interval)

    elapsed = time.time() - start_time
    error_detail = f" ({str(last_exception)})" if last_exception else ""
    raise TimeoutException(f"{error_message} after {elapsed:.2f} seconds{error_detail}")


def retry_on_exception(func: callable, max_attempts: int = 3, delay: float = 1.0,
                      backoff_factor: float = 2.0, exceptions: Tuple = (Exception,),
                      on_retry: callable = None, **kwargs) -> Any:
    attempt = 1
    last_exception = None
    
    while attempt <= max_attempts:
        try:
            return func(**kwargs)
        except exceptions as e:
            last_exception = e
            if attempt == max_attempts:
                raise
                
            wait_time = delay * (backoff_factor ** (attempt - 1))
            
            if on_retry:
                on_retry(attempt=attempt, exception=e, wait_time=wait_time)
            else:
                logger.warning(
                    "Attempt %d/%d failed with %s: %s. Retrying in %.2fs...",
                    attempt, max_attempts, type(e).__name__, str(e), wait_time
                )
                
            time.sleep(wait_time)
            attempt += 1
            
    if last_exception:
        raise last_exception
    return None

