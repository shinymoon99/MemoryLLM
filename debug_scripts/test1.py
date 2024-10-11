from datasets import load_dataset
from datasets import load_from_disk
from tqdm import tqdm
dataset="hotpotqa"
data = load_from_disk(f"./longbench/data/hotpotqa")

# ds = load_dataset("THUDM/LongBench", "2wikimqa")
# data = load_dataset('THUDM/LongBench', dataset, split='test',trust_remote_code=True)
# data.save_to_disk(f"longbench/data/{dataset}")
# View the first 5 entries
# print(data[0])
# data = data[:5]
i=0
for d in tqdm(data):
    i=i+1 
    print(d)
    if i==1:break
    