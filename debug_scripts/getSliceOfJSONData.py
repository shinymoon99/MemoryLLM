import json

# Load the JSON data
with open("data/versicode_input/downstream_application_code_token_originprompt_dac_Context.json", "r") as f:
    data = json.load(f)

# Take only the first 100 items
first_100_items = data[:100]

# Save the first 100 items to a new JSON file
with open("data/versicode_input/first_100_items_dac.json", "w") as f:
    json.dump(first_100_items, f, indent=2)

print(f"Saved {len(first_100_items)} items to first_100_items.json")

# Optional: Verify the contents of the new file
with open("data/versicode_input/first_100_items_dac.json", "r") as f:
    loaded_data = json.load(f)
    print(f"Loaded {len(loaded_data)} items from the new file")
    print("First item:", loaded_data[0])