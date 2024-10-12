import json

# Input file paths
downstream_file = 'data/VersiCode_Benchmark/code_completion/downstream_application_code/downstream_application_code_block.json'
versicode_file = 'output/versicodeOutput_block_woCT_max64.jsonl'

# Output file path
output_file = 'output/DABlock_woCT_m64.jsonl'

# Load downstream application code block data
with open(downstream_file, 'r', encoding='utf-8') as f:
    downstream_data = json.load(f)

# Create a dictionary of answers and codes indexed by their position
downstream_dict = {i: {"answer": item.get("answer", ""), "code": item.get("code", "")} 
                   for i, item in enumerate(downstream_data['data'])}
versicode_data={"data":[]}
# Process versicode file and add answer and code
with open(versicode_file, 'r', encoding='utf-8') as infile:
    for line in infile:
        ldata = json.loads(line)
        versicode_data["data"].append(ldata)
# Add answer and code to each item in versicode_data
for i, item in enumerate(versicode_data['data']):
    
    if i in downstream_dict:
        item['answer'] = downstream_dict[i]['answer']
        item['code'] = downstream_dict[i]['code']
    else:
        item['answer'] = ""
        item['code'] = ""

# Write the modified data to the output file in normal JSON format
with open(output_file, 'w', encoding='utf-8') as outfile:
    json.dump(versicode_data, outfile, indent=2)

print(f"Modified data has been written to {output_file}")