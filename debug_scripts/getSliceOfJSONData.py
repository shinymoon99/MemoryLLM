import json

input_file_name = "da_token_daContext_prompt1"
output_file_name = "da_token_daContext_prompt1_100sample"
# Load the JSON data
with open(f"data/versicode_input/{input_file_name}.json", "r") as f:
    data = json.load(f)

# Take only the first 100 items
first_100_items = data[:100]

# Save the first 100 items to a new JSON file
with open(f"data/versicode_input/{output_file_name}.json", "w") as f:
    json.dump(first_100_items, f, indent=2)

print(f"Saved {len(first_100_items)} items to first_100_items.json")

# Optional: Verify the contents of the new file
with open(f"data/versicode_input/{output_file_name}.json", "r") as f:
    loaded_data = json.load(f)
    print(f"Loaded {len(loaded_data)} items from the new file")
    print("First item:", loaded_data[0])