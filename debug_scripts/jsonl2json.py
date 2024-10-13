import json
import os

# Define the directory containing the .jsonl files
directory = "output/experiment241013"

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jsonl"):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        # read from line json
        data = []
        with open(file_path, "r") as f:
            for line in f:
                dataout = json.loads(line)
                data.append(dataout)
        # wrap with {"data":readed_data}
        output = {"data": data}
        # Construct the output file path
        output_file_path = file_path.replace(".jsonl", "_e.jsonl")
        # output
        with open(output_file_path, "w") as f1:
            json.dump(output, f1)