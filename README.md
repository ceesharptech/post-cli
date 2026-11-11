# API Inspector

A lightweight command-line HTTP client built with Python's standard library. API Inspector allows developers to construct HTTP requests, send them to endpoints, and inspect the responses directly from their terminal.

## Features

- Supports GET, POST, PUT, PATCH, and DELETE methods.
- Accepts custom HTTP headers.
- Supports JSON request bodies and raw string bodies through the HTTP client.
- Displays HTTP response status codes and reason phrases.
- Displays response headers and bodies.
- Automatically formats valid JSON responses for readability.
- Measures request execution time.
- Handles HTTP error responses separately from connection errors.
- Validates request parameters before execution.

## Technologies

- Python 3.13
- `urllib.request` - constructing and executing HTTP requests.
- `urllib.error` - handling HTTP and connection errors.
- `urllib.parse` - URL parsing and validation.
- `json` - JSON serialisation and deserialisation.
- `time` - measuring request execution time.

No external Python packages are required.

## Project Structure

```text
api-inspector/
├── api_inspector.py
├── http_client.py
├── response_formatter.py
└── README.md
```

### Module Responsibilities

**api_inspector.py**

Handles command-line interactions, collects request parameters, and coordinates the request execution and response formatting.

**http_client.py**

Validates request parameters, constructs HTTP requests, executes network operations, measures execution time, and handles HTTP and connection errors.

**response_formatter.py**

Formats response headers and bodies for terminal display. It also identifies JSON responses and pretty-prints valid JSON content.

## Getting Started

### Requirements

- Python 3.13 or later.

### Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project directory:

```bash
cd api-inspector
```

### Running the Application

Execute the CLI:

```bash
python api_inspector.py
```

Follow the prompts to enter your request method, URL, headers, and request body.

## Example Usage

The following example demonstrates sending a POST request.

**Request**

```http
POST https://jsonplaceholder.typicode.com/posts
Content-Type: application/json
```

Request body:

```json
{
    "title": "Learning HTTP",
    "body": "Building an API Inspector with Python",
    "userId": 1
}
```

**Sample response**

```text
Status Code - 201    Reason - Created
Execution Time - 245.321ms

Response Headers
Content-Type: application/json; charset=utf-8
Content-Length: 120

Response Body
{
    "title": "Learning HTTP",
    "body": "Building an API Inspector with Python",
    "userId": 1,
    "id": 101
}
```

*Response values and execution time are illustrative.*

## Error Handling

API Inspector distinguishes between two major categories of errors:

**HTTP Errors**

Responses such as 400, 404, and 500 are treated as valid HTTP responses. Their status codes, headers, and response bodies are preserved for inspection.

**Connection Errors**

Errors that prevent a successful HTTP response, such as connection failures, are returned separately with an error type and reason.

Invalid request parameters are also validated before the HTTP client attempts execution.

## Current Limitations

- The CLI currently accepts JSON objects as request bodies, although the underlying HTTP client also supports raw strings.
- Response bodies are decoded using UTF-8. Binary responses and other character encodings are not fully supported.
- Request headers are supplied as a dictionary.
- Response formatting is primarily designed for JSON and text-based responses.
- The application does not currently support asynchronous requests or concurrent request execution.

## Learning Objectives

This project was developed to strengthen practical understanding of:

- HTTP request and response structures.
- HTTP methods, headers, and status codes.
- Client-server communication.
- Python's standard networking libraries.
- Request validation and exception handling.
- Modular application architecture.
- Measuring network request execution time.