import json
# get all item with dependency torch and combine its element "answer" into a list
with open('data/downstream_application_code_block.json', 'r') as f:
    data = json.load(f)

torch_data = [item for item in data["data"] if item['dependency'] == 'torch']
torch_answers = [item['answer'] for item in torch_data]

print(torch_answers)
# combine torch_answers with its corresponding poe_api_output item and write into a new json file
with open('data/poe_api_output.json', 'r') as f:
    poe_api_output = json.load(f)

for item in poe_api_output:
    item['answer'] = torch_answers[poe_api_output.index(item)]

with open('data/poe_api_output_with_answer.json', 'w') as f:
    json.dump(poe_api_output, f, indent=2)
