import urllib.request
from urllib.parse import urlparse
import json
import urllib.error
import time


http_request = urllib.request.Request(
    url="https://jsonplaceholder.typicode.com/posts/3",
    method="GET"
)

try:
    # start_time = time.perf_counter()

    # response = urllib.request.urlopen(http_request, timeout=10)
    # response_body = json.dumps(response.read().decode())

    # end_time = time.perf_counter()
    # execution_time = end_time - start_time

    # response_output = {
    #     "status_code": response.getcode(),
    #     "reason": response.reason,
    #     "headers": response.headers,
    #     "body": response_body,
    #     "elapsed_time": execution_time
    # }

    # print(response_output)
    start_time = time.perf_counter()
    with urllib.request.urlopen(http_request, timeout=10) as response:
        response_body = json.dumps(response.read().decode())
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        response_output = {
            "status_code": response.getcode(),
            "reason": response.reason,
            "headers": response.headers,
            "body": response_body,
            "elapsed_time": execution_time
        }

        print(response_output)


except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"Connection error occurred - check your connection")
