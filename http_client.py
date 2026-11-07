import urllib.request
from urllib.parse import urlparse

user_request = {
    "method": "POST",
    "url": "https://example.com/users",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer abc123"
    },
    "body": {
        "name": "John",
        "email": "john@example.com"
    }
}

allowed_methods = {"POST", "GET", "PUT", "PATCH", "DELETE"}
url_schemes = {"http", "https"}
required_parameters = {"method", "url"}

def validate_request(request):
    # Check if required request parameters exist
    missing_params = required_parameters - request.keys()
    method = request["method"].upper()
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
        print("Sent!")
    except (ValueError, TypeError, KeyError) as error:
        print(f"An error occurred: {error}")

send_request(user_request)
