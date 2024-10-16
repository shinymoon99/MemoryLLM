# append context item to /data/versicode/completed_code.json by dependency name and version from /data/version_corpus
import json
import os
from test_version_transform import extract_version
# Read the completed_code.json file
# input_file_name = 'da_block_originprompt'
input_file_name = 'da_token_woCT_prompt1'
data_source = 'downstream_application_code'
with open(f'data/versicode_input/{input_file_name}.json', 'r') as f:
    data = json.load(f)

# Read the template from buildContext.json
with open('longbench_config/buildContext.json', 'r') as template_file:
    template = json.load(template_file)


'''step to add context to completed_code.json'''
# Create a cache directory
cache_dir = f'data/context_cache/{data_source}/version_corpus'
os.makedirs(cache_dir, exist_ok=True)

# Iterate through items in completed_code.json
for item in data:
    dependency = item.get('dependency')
    version = item.get('version')
    # convert version to x.x.x format
    version = extract_version(version)
    if dependency and version:
        # Construct the path to the corresponding corpus file
        corpus_file = f'data/Corpus/{data_source}/version_corpus/{dependency}/{version}.jsonl'
        
        # Construct the path for the cache file
        cache_file = f'{cache_dir}/{dependency}/{version}.json'
        
        if os.path.exists(cache_file):
            # If cache exists, load the context from cache
            with open(cache_file, 'r') as f:
                item['context'] = json.load(f)['context']
        elif os.path.exists(corpus_file):
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
            
            # Save the context to cache
            os.makedirs(os.path.dirname(cache_file), exist_ok=True)
            with open(cache_file, 'w') as f:
                json.dump({'context': combined_context}, f)

# Write the updated data back to completed_code.json
# with open('data/versicode/completed_code.json', 'w') as f:
#     json.dump(data, f, indent=2)

# print("Context has been appended to completed_code.json")

# with open("longbench/data/versicode/completed_code.json", "r") as f:
#     data = json.load(f)


# '''step to add features in order to be compatible with longbench'''
# # Modify each item in the list
# for item in data:
#     # Add new elements
#     item['length'] = 8616
#     item['dataset'] = 'versicode'
#     item['language'] = 'en'
#     item['all_classes'] = None
#     item['_id'] = str(data.index(item))  # Use index as _id
    
#     # Convert 'answer' to 'answers' list
#     item['answers'] = [item.pop('answer')]

# Save the modified data back to the JSON file
with open(f"data/versicode_input/{input_file_name}_daContext.json", "w") as f:
    json.dump(data, f, indent=2)

print("JSON file has been updated successfully.")