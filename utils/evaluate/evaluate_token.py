"""
pass@k Indicator to evaluate the ability of token level
"""

import json
import os
import math

model_name = 'Llama-3-70b-chat-hf'

result_path = f'output/versicodeOutput_token_dac.jsonl'
# result_path = f'../../dataset/final_dataset/final_generate_token_result/{model_name}/docstring.json'
# result_path = f'../../dataset/final_dataset/final_generate_token_result/{model_name}/respository.json'
# result_path = f'../../dataset/final_dataset/final_generate_token_result/{model_name}/stackoverflow.json'
def compute_score_k(answer:str, model_output:list, k:int):

    c = 0
    n = len(model_output)
    for output in model_output:
        if answer == output:
            c += 1
    if n-c<k:
        return 1.0

    score = 1 - (math.comb(n - c, k))/(math.comb(n, k))

    return score



# with open(result_path, 'r', encoding='utf-8')as fr:
#     lodict = json.load(fr)
# data = lodict

# data_list = data['data']
data_list = []
with open(result_path, 'r', encoding='utf-8') as fr:
    for line in fr:
        data_list.append(json.loads(line))
score_list = []

for d in data_list[:100]:
    answer = d['answer']
    # for one sample, copy it 6 times,which means 6 times of the same answer stripped of external brackets
    model_output_list = eval(d['model_output_token_clear'])#change block or token or line
    # model_output_list = model_output_list*6
    temp_score = compute_score_k(answer, model_output_list[:6], 1)
    score_list.append(temp_score)


# print(sum(score_list))
final_score = sum(score_list)/len(score_list)

print(final_score)
