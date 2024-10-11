import requests

url = "https://api.together.xyz/v1/chat/completions"

payload = {
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant"
        },
        {
            "role": "user",
            "content": "What is 1 + 1?"
        }
    ],
    "model": "mistralai/Mixtral-8x7B-Instruct-v0.1"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": ""
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)