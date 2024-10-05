from datasets import Dataset, DatasetDict
import json
from datasets import load_from_disk
# Load the JSON data
# with open("longbench/data/versicode/completed_code.json", "r") as f:
#     data = json.load(f)

# # Create a Dataset object
# dataset = Dataset.from_list(data)

# # Create a DatasetDict with a single split (e.g., "train")
# dataset_dict = DatasetDict({"train": dataset})

# # Save the DatasetDict to disk
# dataset_dict.save_to_disk("longbench/data/versicode")

# Now you can load it using load_from_disk
data = load_from_disk("longbench/data/versicode")
print(data)