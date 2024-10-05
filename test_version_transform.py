import os
import json
import re

def extract_version(version_string):
    # Simpler regex pattern to capture the version number
    pattern = r'([\d.]+)'
    
    match = re.search(pattern, version_string)
    
    if match:
        version_num = match.group(1)  # Return the captured version number
        # append .0 if version_num is not in x.y.z format
        if not re.match(r'\d+\.\d+\.\d+', version_num):
            version_num += '.0'
        return version_num
    return None  # Return None if no match found

# ... (rest of the code remains unchanged)

# Read the completed_code.json file
with open('data/versicode/completed_code.json', 'r') as f:
    data = json.load(f)

# Iterate through items in completed_code.json
for item in data:
    version = item.get('version')

    # Extract the version number
    version_num = extract_version(version)

    # Print the input and output
    # print(f"input: {version}")
    # print(f"output: {version_num}")
    # print()  # Add a blank line for readability between entries