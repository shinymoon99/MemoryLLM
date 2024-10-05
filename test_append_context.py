# append context item to /data/versicode/completed_code.json by dependency name and version from /data/version_corpus
import json
import os
from test_version_transform import extract_version
# Read the completed_code.json file
with open('data/versicode/completed_code.json', 'r') as f:
    data = json.load(f)

# Read the template from buildContext.json
with open('longbench_config/buildContext.json', 'r') as template_file:
    template = json.load(template_file)

# Iterate through items in completed_code.json
for item in data:
    dependency = item.get('dependency')
    version = item.get('version')
    # convert version to x.x.x format
    version = extract_version(version)
    if dependency and version:
        # Construct the path to the corresponding corpus file
        corpus_file = f'data/version_corpus/{dependency}/{version}.jsonl'
        
        if os.path.exists(corpus_file):
            contexts = []
            with open(corpus_file, 'r') as jsonl_file:
                for line in jsonl_file:
                    if line.strip():  # Skip empty lines
                        jsonl_data = json.loads(line)
                        context = template['versicode'].format(
                            file_path=jsonl_data['file_path'],
                            source_code=jsonl_data['source_code']
                        )
                        contexts.append(context)
            
            # Combine all contexts
            combined_context = "\n".join(contexts)
            # Truncate combined_context to 15000 words
            words = combined_context.split()
            if len(words) > 15000:
                combined_context = ' '.join(words[:15000])

            # Append the combined context to the item
            item['context'] = combined_context

# Write the updated data back to completed_code.json
with open('data/versicode/completed_code.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Context has been appended to completed_code.json")
