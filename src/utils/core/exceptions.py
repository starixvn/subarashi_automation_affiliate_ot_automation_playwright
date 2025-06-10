from typing import Optional, Any, Dict, List, Union
from datetime import datetime
import traceback
import json

class AutomationException(Exception):
    def __init__(
        self,
        message: str,
        details: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        original_exception: Optional[Exception] = None,
        operation: str = "unknown",
        test_case: Optional[str] = None,
    ):
        self.message = message
        self.details = details or ""
        self.context = context or {}
        self.original_exception = original_exception
        self.operation = operation
        self.test_case = test_case
        self.timestamp = datetime.now()
        self.traceback = traceback.format_exc() if original_exception else ""

        error_message = f"{message}"
        if details:
            error_message += f"\nDetails: {details}"
        if original_exception:
            error_message += f"\nOriginal exception: {str(original_exception)}"

        super().__init__(error_message)

    def __str__(self) -> str:
        return self.message

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self.__class__.__name__,
            'message': self.message,
            'details': self.details,
            'context': self.context,
            'operation': self.operation,
            'test_case': self.test_case,
            'timestamp': self.timestamp.isoformat(),
            'original_exception': str(self.original_exception) if self.original_exception else None
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, default=str)

    def get_full_message(self, include_traceback: bool = False) -> str:

        parts = [f"Error: {self.message}"]

        if self.details:
            parts.append(f"Details: {self.details}")

        if self.context:
            parts.append(f"Context: {json.dumps(self.context, indent=2, default=str)}")

        if self.operation != "unknown":
            parts.append(f"Operation: {self.operation}")

        if self.test_case:
            parts.append(f"Test Case: {self.test_case}")

        if self.original_exception:
            parts.append(f"Original Exception: {self.original_exception.__class__.__name__}: {str(self.original_exception)}")

        if include_traceback and self.traceback:
            parts.append(f"Traceback:\n{self.traceback}")

        return "\n".join(parts)

class ValidationException(AutomationException):
    def __init__(
        self,
        message: str,
        field_name: Optional[str] = None,
        expected_value: Any = None,
        actual_value: Any = None,
        validation_rule: Optional[str] = None,
        **kwargs
    ):
        context = kwargs.get('context', {})
        if field_name:
            context['field_name'] = field_name
        if expected_value is not None:
            context['expected_value'] = str(expected_value)
        if actual_value is not None:
            context['actual_value'] = str(actual_value)
        if validation_rule:
            context['validation_rule'] = validation_rule

        kwargs['context'] = context

        if 'details' not in kwargs or not kwargs['details']:
            details_parts = []
            if field_name:
                details_parts.append(f"Field: {field_name}")
            if expected_value is not None and actual_value is not None:
                details_parts.append(f"Expected: {expected_value}, Actual: {actual_value}")
            elif validation_rule:
                details_parts.append(f"Rule: {validation_rule}")

            if details_parts:
                kwargs['details'] = ", ".join(details_parts)

        super().__init__(message, **kwargs)

        self.field_name = field_name
        self.expected_value = expected_value
        self.actual_value = actual_value
        self.validation_rule = validation_rule

class AssertionException(ValidationException):
    def __init__(
        self,
        message: str,
        assertion: Optional[str] = None,
        **kwargs
    ):
        if assertion:
            if 'context' not in kwargs:
                kwargs['context'] = {}
            kwargs['context']['assertion'] = assertion

        super().__init__(message, **kwargs)
        self.assertion = assertion

class ServiceException(AutomationException):
    def __init__(
        self,
        message: str,
        service_name: Optional[str] = None,
        request_info: Optional[Dict[str, Any]] = None,
        response_info: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        context = kwargs.get('context', {})
        if service_name:
            context['service_name'] = service_name
        if request_info:
            context['request'] = request_info
        if response_info:
            context['response'] = response_info

        kwargs['context'] = context

        super().__init__(message, **kwargs)

        self.service_name = service_name
        self.request_info = request_info
        self.response_info = response_info

class ApiException(ServiceException):
    def __init__(
        self,
        message: str,
        url: Optional[str] = None,
        method: Optional[str] = None,
        status_code: Optional[int] = None,
        response_body: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        request_info = None
        if url or method or headers:
            request_info = {
                'url': url,
                'method': method,
                'headers': headers
            }

        response_info = None
        if status_code is not None or response_body:
            response_info = {
                'status_code': status_code,
                'body': response_body
            }

        super().__init__(
            message,
            service_name="API",
            request_info=request_info,
            response_info=response_info,
            **kwargs
        )

        self.url = url
        self.method = method
        self.status_code = status_code
        self.response_body = response_body
        self.headers = headers

class DatabaseException(ServiceException):
    def __init__(
        self,
        message: str,
        query: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        db_name: Optional[str] = None,
        error_code: Optional[str] = None,
        **kwargs
    ):
        request_info = None
        if query or parameters:
            request_info = {
                'query': query,
                'parameters': parameters
            }

        if 'details' not in kwargs or not kwargs['details']:
            details_parts = []
            if db_name:
                details_parts.append(f"Database: {db_name}")
            if error_code:
                details_parts.append(f"Error code: {error_code}")
            if query:
                details_parts.append(f"Query: {query}")

            if details_parts:
                kwargs['details'] = ", ".join(details_parts)

        super().__init__(
            message,
            service_name=f"Database{f' ({db_name})' if db_name else ''}",
            request_info=request_info,
            **kwargs
        )

        self.query = query
        self.parameters = parameters
        self.db_name = db_name
        self.error_code = error_code

class BrowserException(ServiceException):
    def __init__(
        self,
        message: str,
        url: Optional[str] = None,
        browser_name: Optional[str] = None,
        browser_version: Optional[str] = None,
        **kwargs
    ):
        context = kwargs.get('context', {})
        if url:
            context['url'] = url
        if browser_name:
            context['browser_name'] = browser_name
        if browser_version:
            context['browser_version'] = browser_version

        kwargs['context'] = context

        super().__init__(
            message,
            service_name=f"Browser{f' ({browser_name})' if browser_name else ''}",
            **kwargs
        )

        self.url = url
        self.browser_name = browser_name
        self.browser_version = browser_version

class ElementException(BrowserException):
    def __init__(
        self,
        message: str,
        selector: Optional[str] = None,
        element_text: Optional[str] = None,
        element_attributes: Optional[Dict[str, str]] = None,
        iframe_context: Optional[str] = None,
        **kwargs
    ):
        self.selector = selector
        self.element_text = element_text
        self.element_attributes = element_attributes
        self.iframe_context = iframe_context

        context = kwargs.get('context', {})
        if selector:
            context['selector'] = selector
        if element_text:
            context['element_text'] = element_text
        if element_attributes:
            context['element_attributes'] = element_attributes
        if iframe_context:
            context['iframe_context'] = iframe_context

        kwargs['context'] = context

        if 'details' not in kwargs or not kwargs['details']:
            details_parts = []
            if selector:
                details_parts.append(f"Selector: {selector}")
            if iframe_context:
                details_parts.append(f"iFrame: {iframe_context}")
            if element_text:
                text_preview = element_text[:50] + ('...' if len(element_text) > 50 else '')
                details_parts.append(f"Element text: {text_preview}")

            if details_parts:
                kwargs['details'] = ", ".join(details_parts)

        super().__init__(message, **kwargs)

class ElementNotFoundException(ElementException):
    def __init__(
        self,
        message: str = "Element not found",
        timeout: Optional[float] = None,
        **kwargs
    ):
        if timeout is not None:
            if 'context' not in kwargs:
                kwargs['context'] = {}
            kwargs['context']['timeout'] = timeout

            if 'details' not in kwargs or not kwargs['details']:
                kwargs['details'] = f"Element not found after waiting {timeout} seconds"

        super().__init__(message, **kwargs)
        self.timeout = timeout

class ElementStateException(ElementException):
    def __init__(
        self,
        message: str,
        expected_state: Optional[str] = None,
        actual_state: Optional[str] = None,
        **kwargs
    ):
        if expected_state or actual_state:
            context = kwargs.get('context', {})
            if expected_state:
                context['expected_state'] = expected_state
            if actual_state:
                context['actual_state'] = actual_state
            kwargs['context'] = context

            if 'details' not in kwargs or not kwargs['details']:
                if expected_state and actual_state:
                    kwargs['details'] = f"Expected state: {expected_state}, Actual: {actual_state}"
                elif expected_state:
                    kwargs['details'] = f"Expected state: {expected_state}"

        super().__init__(message, **kwargs)
        self.expected_state = expected_state
        self.actual_state = actual_state

class NavigationException(BrowserException):
    def __init__(
        self,
        message: str,
        target_url: Optional[str] = None,
        current_url: Optional[str] = None,
        status_code: Optional[int] = None,
        **kwargs
    ):
        if target_url or current_url or status_code is not None:
            context = kwargs.get('context', {})
            if target_url:
                context['target_url'] = target_url
            if current_url:
                context['current_url'] = current_url
            if status_code is not None:
                context['status_code'] = status_code
            kwargs['context'] = context

            if 'details' not in kwargs or not kwargs['details']:
                details_parts = []
                if target_url:
                    details_parts.append(f"Target URL: {target_url}")
                if current_url:
                    details_parts.append(f"Current URL: {current_url}")
                if status_code is not None:
                    details_parts.append(f"Status code: {status_code}")

                if details_parts:
                    kwargs['details'] = ", ".join(details_parts)

        super().__init__(message, url=target_url, **kwargs)
        self.target_url = target_url
        self.current_url = current_url
        self.status_code = status_code

class PageException(BrowserException):
    def __init__(
        self,
        message: str,
        url: Optional[str] = None,
        operation_type: Optional[str] = None,
        resource_type: Optional[str] = None,
        resource_url: Optional[str] = None,
        **kwargs
    ):
        if not kwargs.get('url') and url:
            kwargs['url'] = url

        context = kwargs.get('context', {})
        if operation_type:
            context['operation_type'] = operation_type
        if resource_type:
            context['resource_type'] = resource_type
        if resource_url:
            context['resource_url'] = resource_url

        kwargs['context'] = context

        if 'details' not in kwargs or not kwargs['details']:
            details_parts = []
            if url:
                details_parts.append(f"URL: {url}")
            if operation_type:
                details_parts.append(f"Operation: {operation_type}")
            if resource_type and resource_url:
                details_parts.append(f"{resource_type.capitalize()}: {resource_url}")

            if details_parts:
                kwargs['details'] = ", ".join(details_parts)

        super().__init__(message, **kwargs)

        self.url = url
        self.operation_type = operation_type
        self.resource_type = resource_type
        self.resource_url = resource_url

class TimeoutException(BrowserException):
    def __init__(
        self,
        message: str = "Operation timed out",
        timeout: Optional[float] = None,
        operation_type: Optional[str] = None,
        **kwargs
    ):
        if timeout is not None or operation_type:
            context = kwargs.get('context', {})
            if timeout is not None:
                context['timeout'] = timeout
            if operation_type:
                context['operation_type'] = operation_type
            kwargs['context'] = context

            if 'details' not in kwargs or not kwargs['details']:
                if timeout is not None and operation_type:
                    kwargs['details'] = f"{operation_type} timed out after {timeout} seconds"
                elif timeout is not None:
                    kwargs['details'] = f"Operation timed out after {timeout} seconds"
                elif operation_type:
                    kwargs['details'] = f"{operation_type} timed out"

        super().__init__(message, **kwargs)
        self.timeout = timeout
        self.operation_type = operation_type

class ConfigException(AutomationException):
    def __init__(
        self,
        message: str,
        config_key: Optional[str] = None,
        config_file: Optional[str] = None,
        config_value: Optional[Any] = None,
        **kwargs
    ):
        if config_key or config_file or config_value is not None:
            context = kwargs.get('context', {})
            if config_key:
                context['config_key'] = config_key
            if config_file:
                context['config_file'] = config_file
            if config_value is not None:
                context['config_value'] = str(config_value)
            kwargs['context'] = context

            if 'details' not in kwargs or not kwargs['details']:
                details_parts = []
                if config_key:
                    details_parts.append(f"Config key: {config_key}")
                if config_file:
                    details_parts.append(f"Config file: {config_file}")
                if config_value is not None:
                    details_parts.append(f"Value: {config_value}")

                if details_parts:
                    kwargs['details'] = ", ".join(details_parts)

        super().__init__(message, **kwargs)
        self.config_key = config_key
        self.config_file = config_file
        self.config_value = config_value

class IoException(AutomationException):
    def __init__(
        self,
        message: str,
        path: Optional[str] = None,
        io_operation: Optional[str] = None,
        **kwargs
    ):
        if path or io_operation:
            context = kwargs.get('context', {})
            if path:
                context['path'] = path
            if io_operation:
                context['io_operation'] = io_operation
            kwargs['context'] = context

            if 'details' not in kwargs or not kwargs['details']:
                details_parts = []
                if io_operation and path:
                    details_parts.append(f"{io_operation} operation failed on path: {path}")
                elif path:
                    details_parts.append(f"Path: {path}")
                elif io_operation:
                    details_parts.append(f"Operation: {io_operation}")

                if details_parts:
                    kwargs['details'] = ", ".join(details_parts)

        super().__init__(message, **kwargs)
        self.path = path
        self.io_operation = io_operation

class FileException(IoException):
    def __init__(
        self,
        message: str,
        file_path: Optional[str] = None,
        file_size: Optional[int] = None,
        file_type: Optional[str] = None,
        **kwargs
    ):
        if 'io_operation' not in kwargs:
            if "not found" in message.lower():
                kwargs['io_operation'] = "read"
            elif "permission" in message.lower():
                kwargs['io_operation'] = "access"
            elif "create" in message.lower():
                kwargs['io_operation'] = "write"

        context = kwargs.get('context', {})
        if file_size is not None:
            context['file_size'] = file_size
        if file_type:
            context['file_type'] = file_type
        kwargs['context'] = context

        super().__init__(message, path=file_path, **kwargs)
        self.file_path = file_path
        self.file_size = file_size
        self.file_type = file_type

class NetworkException(IoException):
    def __init__(
        self,
        message: str,
        host: Optional[str] = None,
        port: Optional[int] = None,
        protocol: Optional[str] = None,
        status_code: Optional[int] = None,
        **kwargs
    ):
        context = kwargs.get('context', {})
        if host:
            context['host'] = host
        if port is not None:
            context['port'] = port
        if protocol:
            context['protocol'] = protocol
        if status_code is not None:
            context['status_code'] = status_code
        kwargs['context'] = context

        path = kwargs.get('path')
        if not path and host:
            path = f"{protocol or 'http'}://{host}"
            if port:
                path += f":{port}"

        super().__init__(message, path=path, **kwargs)
        self.host = host
        self.port = port
        self.protocol = protocol
        self.status_code = status_code

class NotificationException(ServiceException):
    def __init__(
        self,
        message: str,
        channel: Optional[str] = None,
        recipient: Optional[Union[str, List[str]]] = None,
        notification_type: Optional[str] = None,
        **kwargs
    ):
        context = kwargs.get('context', {})
        if channel:
            context['channel'] = channel
        if recipient:
            context['recipient'] = recipient
        if notification_type:
            context['notification_type'] = notification_type
        kwargs['context'] = context

        if 'details' not in kwargs or not kwargs['details']:
            details_parts = []
            if channel:
                details_parts.append(f"Channel: {channel}")
            if recipient:
                if isinstance(recipient, list):
                    details_parts.append(f"Recipients: {', '.join(recipient)}")
                else:
                    details_parts.append(f"Recipient: {recipient}")
            if notification_type:
                details_parts.append(f"Type: {notification_type}")

            if details_parts:
                kwargs['details'] = ", ".join(details_parts)

        super().__init__(
            message,
            service_name=f"Notification{f' ({channel})' if channel else ''}",
            **kwargs
        )
        self.channel = channel
        self.recipient = recipient
        self.notification_type = notification_type

def create_exception(
    exception_type: type,
    message: str,
    details: Optional[str] = None,
    context: Optional[Dict[str, Any]] = None,
    original_exception: Optional[Exception] = None,
    operation: str = "unknown",
    test_case: Optional[str] = None,
    **kwargs
) -> AutomationException:
    return exception_type(
        message=message,
        details=details,
        context=context,
        original_exception=original_exception,
        operation=operation,
        test_case=test_case,
        **kwargs
    )


