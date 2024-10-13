from datasets import Dataset
import json

# Load the JSON data
with open("data/versicode_input/da_block_originprompt_dac_Context.json", "r") as f:
    data = json.load(f)

# Create a Dataset object
dataset = Dataset.from_list(data)

# Save the Dataset to disk
dataset.save_to_disk("longbench/data/versicode/da_block_da")

# # Now you can load it using load_from_disk
from datasets import load_from_disk
loaded_dataset = load_from_disk("longbench/data/versicode/da_block_da")
print(loaded_dataset[:1])