


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



# # Self-Update with the new context
# ctx = "Last week, John had a wonderful picnic with David. During their conversation, David mentioned multiple times that he likes eating apples. Though he didn't mention any other fruits, John says he can infer that David also like bananas."

# # please make sure the context to inject into the memory is larger than 16 tokens, this is the hard minimum when training the model. The memory will be disturbed when less than 16 tokens are injected into the memory. 
# model.inject_memory(tokenizer(ctx, return_tensors='pt', add_special_tokens=False).input_ids.cuda(), update_memory=True)
# inputs = tokenizer("Question: What fruits does David like? Answer: David likes", return_tensors='pt', add_special_tokens=False).input_ids.cuda()
# outputs = model.generate(input_ids=inputs, max_new_tokens=20)
# response = tokenizer.decode(outputs[0][inputs.shape[1]:])
# print("response:",response)

# 猜想1:给定相应功能描述知识的时候，模型能根据这些知识激活本身coding知识并结合提供的知识加以应用(COT)。
# Self-Update with the new context
ctx = """
numpy.zeros(shape, dtype=float, order='C', *, like=None) Return a new array of given shape and type, filled with zeros. 
"""
input_untokenized ="""
You are a professional Python engineer, and I will provide functional descriptions and versions of specified dependency packages. \nYou need to write code in Python to implement this feature based on the functional description and using the dependency package and version I specified. \nPlease note that you only need to return the code that implements the function, and do not return any other content. \nPlease use <start> and <end> to enclose the generated code. Here is an example:\n###Function Description:\nThe function of this code is to print the results predicted by calling the model using vllm.\n###dependency and version:\nvllm==0.3.3\n###response:\n<start>\n for output in outputs:\n    prompt = output.prompt\n    generated_text = output.outputs[0].text\n    print(\"Prompt,Generated text\")\n<end>\n\nGiven above example, please generate answer code given below requirement.###Function Description:\nThis function generates a one-hot encoded array based on the input label within the provided dimension.\n###dependency and version:\nnumpy==1.14.3\n

"""
# please make sure the context to inject into the memory is larger than 16 tokens, this is the hard minimum when training the model. The memory will be disturbed when less than 16 tokens are injected into the memory. 
model.inject_memory(tokenizer(ctx, return_tensors='pt', add_special_tokens=False).input_ids.cuda(), update_memory=True)
inputs = tokenizer(input_untokenized, return_tensors='pt', add_special_tokens=False).input_ids.cuda()
outputs = model.generate(input_ids=inputs, max_new_tokens=128)
response = tokenizer.decode(outputs[0][inputs.shape[1]:])
print("response:",response)