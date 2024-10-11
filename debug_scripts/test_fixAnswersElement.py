import json
import jsonlines
# Load the downstream_application_code_token.json file
with open('data/VersiCode_Benchmark/code_completion/downstream_application_code/downstream_application_code_token.json', 'r',encoding='utf-8') as file:
    downstream_data = json.load(file)

# Extract answers from downstream_application_code_token.json
downstream_answers = [item['answer'] for item in downstream_data["data"]]

# Load and update the versicode.jsonl file
updated_data = []
with jsonlines.open('longbench/pred_seed0/memoryllm-8b_12384/versicode_nocontext.jsonl', 'r') as reader:
    for index, item in enumerate(reader):
        if index < len(downstream_answers):
            item['answers'] = [downstream_answers[index]]
        updated_data.append(item)

# Save the modified data back to versicode.jsonl
with jsonlines.open('longbench/pred_seed0/memoryllm-8b_12384/versicode_nocontext_fix.jsonl', 'w') as writer:
    writer.write_all(updated_data)

print("File has been successfully updated.")