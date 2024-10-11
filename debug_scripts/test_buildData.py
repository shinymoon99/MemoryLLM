import json

# Load the JSON file
with open('data/downstream_application_code_block.json', 'r') as file:
    data = json.load(file)

# Generate input for each item in the JSON data
# for item in data['data']:
#     input_text = f"description:{item['description']},masked_code:{item['masked_code']}"
    
#     print("Input for test_poeAPI:")
#     print(input_text)
#     print("\n" + "-"*50 + "\n")

# Optionally, you can save these inputs to a file
with open('poe_api_inputs.txt', 'w') as output_file:
    for item in data['data']:
        if item['dependency'] == 'torch':
            input_text = f"description:\n{item['description']}\nmasked_code:\n{item['masked_code']}"
            output_file.write(input_text + "\n<item_end>\n\n")

print("Inputs have been generated and saved to 'poe_api_inputs.txt'")