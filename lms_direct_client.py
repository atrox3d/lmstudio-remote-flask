import requests

# Define the LM Studio API URL
API_URL = "http://localhost:1234/v1/chat/completions"

# Set up the headers and payload for the request
headers = {
    "Content-Type": "application/json",
    # Include Authorization header if required
}

payload = {
    "model": "meta-llama-3.1-8b-instruct",  # Replace with your model's identifier
    "messages": [
        {"role": "user", "content": "hello"}
    ],
    "stream": True  # Enable streaming
}

try:
    # Send the POST request with streaming enabled
    response = requests.post(API_URL, headers=headers, json=payload, stream=True)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Process the streamed response
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            print(decoded_line)  # Process the decoded line as needed

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
