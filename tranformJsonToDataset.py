from datasets import Dataset
import json
output_dir="da_token_daContext_prompt1_100sample"
# Load the JSON data
with open(f"data/versicode_input/{output_dir}.json", "r") as f:
    data = json.load(f)

# Create a Dataset object
dataset = Dataset.from_list(data)

# Save the Dataset to disk
dataset.save_to_disk(f"longbench/data/versicode/{output_dir}")

# # Now you can load it using load_from_disk
from datasets import load_from_disk
loaded_dataset = load_from_disk(f"longbench/data/versicode/{output_dir}")
print(loaded_dataset[0])