import json
from collections import defaultdict

# Read the JSON file
with open('data/versicode/completed_code.json', 'r') as f:
    data = json.load(f)

# Dictionary to store dependencies and their versions
dependencies = defaultdict(set)

# Iterate through the data and collect dependencies
for item in data:
    if 'dependency' in item and 'version' in item:
        dependencies[item['dependency']].add(item['version'])

# Print the dependencies
print("Dependencies found in completed_code.json:")
print("------------------------------------------")
for dep, versions in sorted(dependencies.items()):
    versions_str = ', '.join(sorted(versions))
    print(f"{dep}: {versions_str}")
# Create dependency corpus folders by their dependency name under data/version_corpus
import os

# Create the base directory if it doesn't exist
base_dir = 'data/version_corpus'
os.makedirs(base_dir, exist_ok=True)

# Create a folder for each dependency
for dep in dependencies.keys():
    dep_dir = os.path.join(base_dir, dep)
    os.makedirs(dep_dir, exist_ok=True)

print(f"\nCreated dependency corpus folders in {base_dir}")
