import json
import os

# Read the template from buildContext.json
with open('longbench_config/buildContext.json', 'r') as template_file:
    template = json.load(template_file)

# Read the 0.2.0.jsonl file
contexts = []
with open('data/corpus/0.2.0.jsonl', 'r') as jsonl_file:
    for line in jsonl_file:
        if line.strip():  # Skip empty lines
            data = json.loads(line)
            context = template['versicode'].format(
                file_path=data['file_path'],
                source_code=data['source_code']
            )
            contexts.append(context)

# Combine all contexts
combined_context = "\n".join(contexts)

# Create a directory for the output if it doesn't exist
output_dir = './data/combined_contexts'
os.makedirs(output_dir, exist_ok=True)

# Write the combined context to a file
output_file = os.path.join(output_dir, 'accelerate_0.2.0_context.txt')
with open(output_file, 'w') as f:
    f.write(combined_context)

print(f"Combined context has been written to '{output_file}'.")