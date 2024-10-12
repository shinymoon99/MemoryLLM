import json
import os

# Read the template from buildfromVC.json
with open('longbench_config/buildfromVC.json', 'r',encoding="utf-8") as template_file:
    template = json.load(template_file)

# Read the JSON data
with open('data/VersiCode_Benchmark/code_completion/downstream_application_code/downstream_application_code_block.json', 'r',encoding='utf-8') as f:
    data = json.load(f)

# Create a directory for the output if it doesn't exist
output_dir = './data/versicode_input/'
os.makedirs(output_dir, exist_ok=True)

# Process each item in the data and collect all outputs
output_data = []
for item in data['data']:
    description = item.get('description', '')
    code = item.get('code', '')
    answer = item.get('answer', '')
    # masked_code = item.get('masked_code', '')
    # answer = item.get('answer', '')
    dependency = item.get('dependency', '')
    version = item.get('version', '')
    id = item.get('id', '')
    dependency_with_version = f"{dependency}{version}"
    # Create the prompt using the template
    input = template['versicode_origin_prompt_block'].format(description=description, masked_code=code, dependency=dependency, version=dependency_with_version)
    context = ""
    
    output_data.append({
        "input": input,
        "context": context,
        "masked_code":code,
        "answer": answer,
        "dependency": dependency,
        "version": version,
        "description": description,
        "length": 8616,
        "dataset": "versicode",
        "language": "en",
        "all_classes": None,
        "id": id
    })

# Write all outputs to a single JSON file
output_file = os.path.join(output_dir, "da_block_originprompt.json")
with open(output_file, 'w') as f:
    json.dump(output_data, f, indent=2)

print(f"JSON file has been created at '{output_file}'.")