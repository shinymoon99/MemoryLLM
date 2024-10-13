import json
import os
from glob import glob

model_name = 'Llama-3-70b-chat-hf'
result_dir = 'output/experiment241013'

for result_path in glob(os.path.join(result_dir, '*_e.jsonl')):
    result_out = result_path.replace('_e.jsonl', '_m.jsonl')
    with open(result_path, 'r', encoding='utf-8') as fr:
        lodict = json.load(fr)
    data_dict = lodict
    data_list = data_dict['data']

    for data in data_list:
        temp_list = []
        model_output_list = [data['model_output']]
        for output in model_output_list:

            if "<start>" in output:
                start_index = output.find("<start>") + len("<start>")
                if "<end>" in output:
                    end_index = output.find("<end>")
                    content = output[start_index:end_index].replace('```python', '').replace('```', '')
                else:
                    content = output[start_index:].replace('```python', '').replace('```', '')
            else:
                content = "no_answer"

            temp_list.append(content)

        data['model_output_block_clear'] = str(temp_list)

    with open(result_out, 'w', encoding='utf-8') as fw:
        json.dump(data_dict, fw, indent=4, ensure_ascii=False)