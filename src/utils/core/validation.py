import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

from src.utils.core.exceptions import ValidationException


def validate_not_none(value: Any, name: str = "value") -> Any:
    if value is None:
        raise ValidationException(f"{name} cannot be None")
    return value


def validate_not_empty(value: Union[str, List, Dict, Tuple], name: str = "value") -> Any:
    validate_not_none(value, name)
    
    if not value:
        raise ValidationException(f"{name} cannot be empty")
    return value


def validate_type(
    value: Any, 
    expected_type: Union[Type, Tuple[Type, ...]], 
    name: str = "value"
) -> Any:
    if not isinstance(value, expected_type):
        if isinstance(expected_type, tuple):
            expected_type_names = [t.__name__ for t in expected_type]
            type_str = f"one of ({', '.join(expected_type_names)})"
        else:
            type_str = expected_type.__name__
            
        raise ValidationException(
            f"{name} must be of type {type_str}, got {type(value).__name__}"
        )
    return value


def validate_range(
    value: Union[int, float],
    min_value: Optional[Union[int, float]] = None,
    max_value: Optional[Union[int, float]] = None,
    name: str = "value"
) -> Union[int, float]:
    validate_type(value, (int, float), name)
    
    if min_value is not None and value < min_value:
        raise ValidationException(f"{name} must be greater than or equal to {min_value}, got {value}")
    
    if max_value is not None and value > max_value:
        raise ValidationException(f"{name} must be less than or equal to {max_value}, got {value}")
    
    return value


def validate_string_pattern(value: str, pattern: str, name: str = "value") -> str:
    validate_type(value, str, name)
    
    if not re.match(pattern, value):
        raise ValidationException(f"{name} must match pattern '{pattern}', got '{value}'")
    
    return value


def validate_file_exists(file_path: Union[str, Path], name: str = "file") -> Path:
    if isinstance(file_path, str):
        file_path = Path(file_path)
    
    validate_type(file_path, Path, name)
    
    if not file_path.exists():
        raise ValidationException(f"{name} at path '{file_path}' does not exist")
    
    if not file_path.is_file():
        raise ValidationException(f"'{file_path}' is not a file")
    
    return file_path


def validate_directory_exists(dir_path: Union[str, Path], name: str = "directory") -> Path:
    if isinstance(dir_path, str):
        dir_path = Path(dir_path)
    
    validate_type(dir_path, Path, name)
    
    if not dir_path.exists():
        raise ValidationException(f"{name} at path '{dir_path}' does not exist")
    
    if not dir_path.is_dir():
        raise ValidationException(f"'{dir_path}' is not a directory")
    
    return dir_path


def validate_callable(value: Any, name: str = "callback") -> Callable:
    if not callable(value):
        raise ValidationException(f"{name} must be callable")
    
    return value


def validate_one_of(value: Any, valid_values: List[Any], name: str = "value") -> Any:

    validate_not_empty(valid_values, "valid_values")
    
    if value not in valid_values:
        raise ValidationException(f"{name} must be one of {valid_values}, got {value}")
    
    return value


def validate_email(email: str, name: str = "email") -> str:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return validate_string_pattern(email, pattern, name)


validate_instance = validate_type


def validate_min_length(value, min_length, message=None):
    return validate_range(
        len(value),
        min_length,
        None,
        message or f"Value length must be at least {min_length}"
    )


def validate_max_length(value, max_length, message=None):
    return validate_range(
        len(value),
        None,
        max_length,
        message or f"Value length must be at most {max_length}"
    )


validate_in_range = validate_range
validate_in_options = validate_one_of
validate_pattern = validate_string_pattern


def validate_url(url, message=None):
    return validate_string_pattern(
        url,
        r"^https?://[^\s/$.?#].[^\s]*$",
        message or "Invalid URL format"
    ) 