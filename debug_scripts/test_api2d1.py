import requests

url = "https://openai.api2d.net/v1/chat/completions"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' 
}

data = {
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": "你好！给我讲个笑话。"}]
}

response = requests.post(url, headers=headers, json=data)
full_response = response.json()["choices"][0]["message"]["content"]
print("Status Code", response.status_code)
print("JSON Response ", response.json())
print("full_response", full_response)