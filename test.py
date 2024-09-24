from modeling_memoryllm import MemoryLLM
from configuration_memoryllm import MemoryLLMConfig
from transformers import AutoTokenizer

# load pretrained model
# model = MemoryLLM.from_pretrained("YuWangX/memoryllm-8b")
# tokenizer = AutoTokenizer.from_pretrained("YuWangX/memoryllm-8b")
# Load model and tokenizer from the local directory
model = MemoryLLM.from_pretrained("../memoryllm-8b")
tokenizer = AutoTokenizer.from_pretrained("../memoryllm-8b")

model = model.bfloat16()
model.config._attn_implementation = 'flash_attention_2'
model = model.cuda()



# Self-Update with the new context
ctx = "Last week, John had a wonderful picnic with David. During their conversation, David mentioned multiple times that he likes eating apples. Though he didn't mention any other fruits, John says he can infer that David also like bananas."

# please make sure the context to inject into the memory is larger than 16 tokens, this is the hard minimum when training the model. The memory will be disturbed when less than 16 tokens are injected into the memory. 
model.inject_memory(tokenizer(ctx, return_tensors='pt', add_special_tokens=False).input_ids.cuda(), update_memory=True)
inputs = tokenizer("Question: What fruits does David like? Answer: David likes", return_tensors='pt', add_special_tokens=False).input_ids.cuda()
outputs = model.generate(input_ids=inputs, max_new_tokens=20)
response = tokenizer.decode(outputs[0][inputs.shape[1]:])
print("response:",response)