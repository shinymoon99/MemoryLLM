import json

# Load the existing JSON data
with open("longbench/data/versicode/completed_code.json", "r") as f:
    data = json.load(f)

# Modify each item in the list
for item in data:
    # Add new elements
    item['length'] = 8616
    item['dataset'] = 'versicode'
    item['language'] = 'en'
    item['all_classes'] = None
    item['_id'] = str(data.index(item))  # Use index as _id
    
    # Convert 'answer' to 'answers' list
    item['answers'] = [item.pop('answer')]

# Save the modified data back to the JSON file
with open("longbench/data/versicode/completed_code1.json", "w") as f:
    json.dump(data, f, indent=2)

print("JSON file has been updated successfully.")