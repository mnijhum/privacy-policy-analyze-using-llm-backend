import requests
import json

# LLaMA API URL
LLAMA_SERVER_URL = "http://127.0.0.1:11434/api/chat"

# Categories to analyze
# 1. Transparency
# 2. Data Control
# 3. Data Security
# 4. Third-Party Sharing
# 5. User Rights

# Function to send a URL and request analysis from LLaMA


def send_url_to_llama(url):
    """
    Send the URL to LLaMA and ask it to fetch and analyze the privacy policy.
    """
    print(f"Sending URL to LLaMA: {url}")
    prompt = f"""
    Please fetch the privacy policy from the URL provided below, analyze the policy, and provide ratings for the following categories on a scale of 1 to 5:
    1. Transparency
    2. Data Control
    3. Data Security
    4. Third-Party Sharing
    5. User Rights

    For each category, provide a score and a brief explanation of why you gave that score. Do not add any extra text Finally give an overall score.
    URL: {url}
    """

    # Payload to send to the LLaMA API
    payload = {
        "model": "llama3.2:latest",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    # Send the request to the LLaMA API
    response = requests.post(LLAMA_SERVER_URL, json=payload, stream=True)

    # Check if the response status is OK
    if response.status_code != 200:
        print(
            f"Error: Failed to get response, status code: {response.status_code}")
        return

    # Initialize an empty string to collect the response chunks
    full_message = ""

    # Iterate over the streamed response
    for line in response.iter_lines():
        if line:
            try:
                # Decode the line and parse the JSON response
                message = line.decode('utf-8')
                message_data = json.loads(message)

                # Extract content from the message
                if 'message' in message_data:
                    content = message_data['message'].get('content', '')
                    # Print each chunk of the response
                    print(f"Chunk: {content}")
                    full_message += content

                # If 'done' is True, we know the response is complete
                if message_data.get('done', False):
                    print("Response complete!")
                    break
            except Exception as e:
                print(f"Error processing line: {e}")
    return full_message
    # Commented out the last three lines


# Example usage
# privacy_url = "https://example.com/privacy-policy"  # Replace with your actual privacy policy URL
# send_url_to_llama(privacy_url)
