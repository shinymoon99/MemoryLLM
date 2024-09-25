from datasets import load_dataset
from datasets import load_from_disk
dataset="hotpotqa"
# data = load_from_disk(f"./data/LongContext/data")

# ds = load_dataset("THUDM/LongBench", "2wikimqa")
data = load_dataset('THUDM/LongBench', dataset, split='test',trust_remote_code=True)
# View the first 5 entries
print(data[:5])