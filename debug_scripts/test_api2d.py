import requests
import json
url = "https://openai.api2d.net/v1/chat/completions"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' # <-- 把 fkxxxxx 替换成你自己的 Forward Key，注意前面的 Bearer 要保留，并且和 Key 中间有一个空格。
}

# data = {
#   "model": "gpt-4o-2024-08-06",
#   "messages": [{"role": "user", "content": "你好！给我讲个笑话。"}]
# }

# response = requests.post(url, headers=headers, json=data)
# # choices  message content
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())
    # Read the JSON file
with open('data/poe_api_output_with_answer.json', 'r') as file:
    data = json.load(file)

# Create a new list to store evaluated items
evaluated_data = []
for item in data:
    if item['output']=='':
        continue
    input_text = item['input']
    output = item['output']
    answer = item['answer']

    prompt = f"a model is asked to do code completion. below is input,model output and ground truth. input:{input_text},model output:{output},ground_truth:{answer}. please evaluate model's performance. If the answer is correct, output <correct>. If the answer is incorrect, according to the error type, if the reasoning process is wrong, output <reasoning error>. Otherwise, if the error is orignated from unfamiliarity with package or package version, output <package unfamiliarity>. So, in conclusion, your answer should be one of below: 1.<correct>   2.<reasoning error>   3.<package unfamiliarity>  .For example, if answer is correct, you should output:<correct>."

    # print(f"Evaluating item...")

    # full_response = ""
    # async for chunk in client.send_message(bot="gpt3_5", message=prompt):
    #     full_response += chunk["response"]

    # print("Evaluation received.")

    data_input = {
      "model": "gpt-4o-2024-08-06",
      "messages": [{"role": "user", "content": prompt}]
    }
    # add a try except stage to handle the error and continue to next item
    try:
        response = requests.post(url, headers=headers, json=data_input)
        full_response = response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error: {e}")
        full_response = ""
        continue
    # Create a new item with the original data and the evaluation
    evaluated_item = {
        "input": input_text,
        "output": output,
        "answer": answer,
        "evaluation": full_response.strip()
    }
    evaluated_data.append(evaluated_item)

# Write the evaluated data to a new JSON file
with open('data/poe_api_evaluated_output.json', 'w') as outfile:
    json.dump(evaluated_data, outfile, indent=2)