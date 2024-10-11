from datasets import Dataset
import json

# Load the JSON data
with open("data/versicode/completed_code_token_origin_prompt_context.json", "r") as f:
    data = json.load(f)


# Create a Dataset object
dataset = Dataset.from_list(data)
print(dataset.select(range(1)))
# # Save the Dataset to disk
# dataset.save_to_disk("longbench/data/versicode")

# # Now you can load it using load_from_disk
# from datasets import load_from_disk
# loaded_dataset = load_from_disk("longbench/data/versicode")
# print(loaded_dataset.select(range(5)))