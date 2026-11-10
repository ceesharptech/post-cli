import urllib.request
from urllib.parse import urlparse
import json
import urllib.error
import time

user_request = {
    "method": "POST",
    "url": "https://jsonplaceholder.typicode.com/posts",
    "headers": {
        "Content-Type": "application/json"
    },
    "body": {
        "title": 'foo',
        "body": 'bar',
        "userId": 1,
  }
}

allowed_methods = {"POST", "GET", "PUT", "PATCH", "DELETE"}
url_schemes = {"http", "https"}
required_parameters = {"method", "url"}

def validate_request(request):
    if not isinstance(request, dict):
        raise TypeError(f"Invalid request format - check request input")
    # Check if required request parameters exist
    missing_params = required_parameters - request.keys()
    headers = request.get("headers", {})
    body = request.get("body")


    if missing_params:
        raise KeyError(f"Missing parameters: {missing_params}")

    # Check if method is valid
    if not isinstance(request["method"], str):
        raise TypeError("Invalid type, method must be a string")
    else:
        method = request["method"].upper()
        if (method not in allowed_methods):
            raise ValueError(f"Invalid request method")

    if not isinstance(request["url"], str):
        raise TypeError(f"URL must be a string")
    else:
        parsed_url = urlparse(request["url"])
        # Check if URL is valid format
        if (parsed_url.scheme not in url_schemes or parsed_url.hostname is None):
            raise ValueError(f"Invalid URL, check URL provided")

    if not isinstance(headers, dict):
        raise TypeError(f"Invalid type, header must be a dict")

    if body is not None and not isinstance(body, (str, dict)):
        raise TypeError(f"Invalid type, body must be a string or dict")

    return True

def send_request(request):
    try:
        validate_request(request)
        method = request["method"].upper()
        url = request["url"]
        headers = request.get("headers", {})
        body = request.get("body")

        if isinstance(body, str):
            request_body = body.encode('utf-8')
        elif body is None:
            request_body = None
        else:
            request_body = json.dumps(body).encode('utf-8')

        http_request = urllib.request.Request(
            url = url,
            data = request_body,
            headers = headers,
            method = method
        )

        start_time = time.perf_counter()

        try:
            with urllib.request.urlopen(http_request, timeout=10) as response:
                response_body = response.read().decode('utf-8')
                response_end_time = time.perf_counter()
                request_execution_time = response_end_time - start_time
                response_output = {
                    "status_code": response.getcode(),
                    "reason": response.reason,
                    "headers": response.headers,
                    "body": response_body,
                    "elapsed_time": request_execution_time
                }

                return response_output

        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8")
            error_end_time = time.perf_counter()
            error_execution_time = error_end_time - start_time
            error_output = {
                "status_code": e.code,
                "reason": e.reason,
                "headers": e.headers,
                "body": error_body,
                "elapsed_time": error_execution_time
            }
            return error_output
        except urllib.error.URLError as e:
            return {
                "error": "ConnectionError",
                "reason": e.reason
            }
    except (ValueError, TypeError, KeyError) as error:
        print(f"An error occurred: {error}")

send_request(user_request)
