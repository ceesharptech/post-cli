import json

def format_headers(headers):
    formatted_headers = []
    
    for key, value in headers.items():
        formatted_headers.append(f"{key}: {value}")
    
    return '\n'.join(formatted_headers)

def format_body(body, content_type):
    if body in ({}, ""):
        return "Empty response body"
    elif body is not None:
 
        media_type = content_type.split(";")[0].strip().lower()
        is_json = (media_type == "application/json" or media_type.endswith("+json"))
        if (is_json):
            try: 
                body_string = json.loads(body)
                return json.dumps(body_string, indent=4)
            except json.JSONDecodeError:
                return body
        elif media_type in ("text/plain", "text/html"):
            return body
        else:
            return body
    else:
        return "No response body"

def format_response(response):
    if "error" in response:
        error_type = response["error"]
        reason = response.get("reason", "Unknown error")

        return f"{error_type}: {reason}"
    else:
        response_body = response.get("body")
        response_headers = response.get("headers", {})
        response_ct = response_headers.get("Content-Type", "")

        formatted_headers = format_headers(response_headers)
        formatted_body = format_body(response_body, response_ct)

        formatted_response = f"Status Code - {response['status_code']} \t Reason - {response['reason']}\nExecution Time - {response['elapsed_time'] * 1000:.3f}ms\n\nResponse Headers\n{formatted_headers}\n\nResponse Body \n{formatted_body}"
        return formatted_response

    
