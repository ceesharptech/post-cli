from http_client import send_request, ValidationError
from response_formatter import format_response
import json

def collect_headers():
    headers = {}
    while True:
        header_input = input("Enter header (Key: Value), or press Enter to finish: ").strip()
        if header_input == "":
            break
        elif not ":" in header_input:
            print("Use a colon (:) to separate key value pair")
        else: 
            key, value = header_input.split(":", 1)
            key = key.strip()
            value = value.strip()
            if not key:
                print("Invalid header - check input and try again\n")
            else:
                headers[key] = value
    return headers

def collect_body():
    while True:
        body_input = input("Enter request body, or press Enter for no body: ").strip()

        if body_input == "":
            return None

        try:
            body = json.loads(body_input)

            if not isinstance(body, dict):
                print("Request body must be a JSON object\n")
                continue

            return body

        except json.JSONDecodeError:
            print("Invalid JSON body - check input and try again\n")

def collect_request():
    method = input("Enter request method: ").strip().upper()
    url = input("Enter request URL: ").strip()
    headers = collect_headers()
    body = collect_body()

    user_request = {
        "method": method,
        "url": url,
        "headers": headers,
        "body": body
    }

    return user_request

def main():
    print("\n================== POST-CLI ==================\n")
    while True:
        user_request = collect_request()
        print("\nSending request...")
        try:
            response = send_request(user_request)
            formatted_response = format_response(response)
            print(f"\n{formatted_response}")
        except ValidationError as error:
            print(f"An error occurred - {error}")

        while True:
            another_request = input("\nSend another request? (y/n): ").strip().lower()
            if not another_request in ('y', 'n'):
                print("Invalid input - enter y or n")
            elif another_request != "y":
                print("\nExiting POST-CLI...")
                return
            else:
                break

if __name__ == "__main__":
    main()
