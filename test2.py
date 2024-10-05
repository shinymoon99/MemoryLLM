import json
import os

# Read the template from buildfromVC.json
with open('longbench_config/buildfromVC.json', 'r') as template_file:
    template = json.load(template_file)

# Read the JSON data
with open('data/VersiCode_Benchmark/code_completion/downstream_application_code/downstream_application_code_block.json', 'r') as f:
    data = json.load(f)

# Create a directory for the output if it doesn't exist
output_dir = './data/versicode/'
os.makedirs(output_dir, exist_ok=True)

# Process each item in the data and collect all outputs
output_data = []
for item in data['data']:
    description = item.get('description', '')
    masked_code = item.get('masked_code', '')
    answer = item.get('masked_line', '')
    dependency = item.get('dependency', '')
    version = item.get('version', '')

    # Create the prompt using the template
    input = template['versicode'].format(description=description, masked_code=masked_code)
    context = ""
    
    output_data.append({
        "input": input,
        "context": context,
        "answer": answer,
        "dependency": dependency,
        "version": version
    })

# Write all outputs to a single JSON file
output_file = os.path.join(output_dir, "completed_code.json")
with open(output_file, 'w') as f:
    json.dump(output_data, f, indent=2)

print(f"JSON file has been created at '{output_file}'.")