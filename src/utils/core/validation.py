"""
Validation utilities for the automation framework.

This module provides functions for validating different types of input data
and ensuring they meet specific constraints. These functions are designed to
fail early with clear error messages when validation fails.
"""
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

from src.utils.core.exceptions import ValidationException


def validate_not_none(value: Any, name: str = "value") -> Any:
    """
    Validate that a value is not None.
    
    Args:
        value: The value to validate
        name: Name of the value for the error message
        
    Returns:
        The validated value
        
    Raises:
        ValidationException: If the value is None
    """
    if value is None:
        raise ValidationException(f"{name} cannot be None")
    return value


def validate_not_empty(value: Union[str, List, Dict, Tuple], name: str = "value") -> Any:
    """
    Validate that a value is not empty.
    
    Args:
        value: The value to validate (string, list, dict, tuple)
        name: Name of the value for the error message
        
    Returns:
        The validated value
        
    Raises:
        ValidationException: If the value is empty
    """
    validate_not_none(value, name)
    
    if not value:
        raise ValidationException(f"{name} cannot be empty")
    return value


def validate_type(
    value: Any, 
    expected_type: Union[Type, Tuple[Type, ...]], 
    name: str = "value"
) -> Any:
    """
    Validate that a value is of the expected type.
    
    Args:
        value: The value to validate
        expected_type: The expected type or tuple of types
        name: Name of the value for the error message
        
    Returns:
        The validated value
        
    Raises:
        ValidationException: If the value is not of the expected type
    """
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
    """
    Validate that a numeric value is within a specified range.
    
    Args:
        value: The numeric value to validate
        min_value: Optional minimum allowed value
        max_value: Optional maximum allowed value
        name: Name of the value for the error message
        
    Returns:
        The validated value
        
    Raises:
        ValidationException: If the value is outside the specified range
    """
    validate_type(value, (int, float), name)
    
    if min_value is not None and value < min_value:
        raise ValidationException(f"{name} must be greater than or equal to {min_value}, got {value}")
    
    if max_value is not None and value > max_value:
        raise ValidationException(f"{name} must be less than or equal to {max_value}, got {value}")
    
    return value


def validate_string_pattern(value: str, pattern: str, name: str = "value") -> str:
    """
    Validate that a string matches a regular expression pattern.
    
    Args:
        value: The string to validate
        pattern: The regular expression pattern to match
        name: Name of the value for the error message
        
    Returns:
        The validated string
        
    Raises:
        ValidationException: If the string doesn't match the pattern
    """
    validate_type(value, str, name)
    
    if not re.match(pattern, value):
        raise ValidationException(f"{name} must match pattern '{pattern}', got '{value}'")
    
    return value


def validate_file_exists(file_path: Union[str, Path], name: str = "file") -> Path:
    """
    Validate that a file exists at the specified path.
    
    Args:
        file_path: Path to the file
        name: Name of the file for the error message
        
    Returns:
        Path object for the validated file
        
    Raises:
        ValidationException: If the file doesn't exist or is not a file
    """
    if isinstance(file_path, str):
        file_path = Path(file_path)
    
    validate_type(file_path, Path, name)
    
    if not file_path.exists():
        raise ValidationException(f"{name} at path '{file_path}' does not exist")
    
    if not file_path.is_file():
        raise ValidationException(f"'{file_path}' is not a file")
    
    return file_path


def validate_directory_exists(dir_path: Union[str, Path], name: str = "directory") -> Path:
    """
    Validate that a directory exists at the specified path.
    
    Args:
        dir_path: Path to the directory
        name: Name of the directory for the error message
        
    Returns:
        Path object for the validated directory
        
    Raises:
        ValidationException: If the directory doesn't exist or is not a directory
    """
    if isinstance(dir_path, str):
        dir_path = Path(dir_path)
    
    validate_type(dir_path, Path, name)
    
    if not dir_path.exists():
        raise ValidationException(f"{name} at path '{dir_path}' does not exist")
    
    if not dir_path.is_dir():
        raise ValidationException(f"'{dir_path}' is not a directory")
    
    return dir_path


def validate_callable(value: Any, name: str = "callback") -> Callable:
    """
    Validate that a value is callable.
    
    Args:
        value: The value to validate
        name: Name of the value for the error message
        
    Returns:
        The validated callable
        
    Raises:
        ValidationException: If the value is not callable
    """
    if not callable(value):
        raise ValidationException(f"{name} must be callable")
    
    return value


def validate_one_of(value: Any, valid_values: List[Any], name: str = "value") -> Any:
    """
    Validate that a value is one of a list of valid values.
    
    Args:
        value: The value to validate
        valid_values: List of valid values
        name: Name of the value for the error message
        
    Returns:
        The validated value
        
    Raises:
        ValidationException: If the value is not in the list of valid values
    """
    validate_not_empty(valid_values, "valid_values")
    
    if value not in valid_values:
        raise ValidationException(f"{name} must be one of {valid_values}, got {value}")
    
    return value


def validate_email(email: str, name: str = "email") -> str:
    """
    Validate that a string is a properly formatted email address.
    
    Args:
        email: The email address to validate
        name: Name of the value for the error message
        
    Returns:
        The validated email string
        
    Raises:
        ValidationException: If the string is not a valid email address
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return validate_string_pattern(email, pattern, name)


# Aliases for convenience
validate_instance = validate_type


def validate_min_length(value, min_length, message=None):
    """
    Validate that a value's length is at least the specified minimum.
    
    Args:
        value: The value with a length (string, list, etc.)
        min_length: The minimum length required
        message: Optional custom error message
        
    Returns:
        The validated value
    """
    return validate_range(
        len(value),
        min_length,
        None,
        message or f"Value length must be at least {min_length}"
    )


def validate_max_length(value, max_length, message=None):
    """
    Validate that a value's length is at most the specified maximum.
    
    Args:
        value: The value with a length (string, list, etc.)
        max_length: The maximum length allowed
        message: Optional custom error message
        
    Returns:
        The validated value
    """
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
    """
    Validate that a string is a properly formatted URL.
    
    Args:
        url: The URL to validate
        message: Optional custom error message
        
    Returns:
        The validated URL string
    """
    return validate_string_pattern(
        url,
        r"^https?://[^\s/$.?#].[^\s]*$",
        message or "Invalid URL format"
    ) 