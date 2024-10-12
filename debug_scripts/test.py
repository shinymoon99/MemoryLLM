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
You are a professional Python engineer, and I will provide functional descriptions and versions of specified dependency packages. \nYou need to write code in Python to implement this feature based on the functional description and using the dependency package and version I specified. \nPlease note that you only need to return the code that implements the function, and do not return any other content. \nPlease use <start> and <end> to enclose the generated code. Here is an example:\n###Function Description:The function of this code is to print the results predicted by calling the model using vllm.\n###dependency and version:vllm==0.3.3\n###response:\n<start>\nfor output in outputs:\n    prompt = output.prompt\n    generated_text = output.outputs[0].text\n    print(\"Prompt,Generated text\")\n<end>\n\n###Function Description:This function generates a one-hot encoded array based on the input label within the provided dimension.\n###dependency and version:numpy==1.14.3\n###response:\n\n
"""
# please make sure the context to inject into the memory is larger than 16 tokens, this is the hard minimum when training the model. The memory will be disturbed when less than 16 tokens are injected into the memory. 
model.inject_memory(tokenizer(ctx, return_tensors='pt', add_special_tokens=False).input_ids.cuda(), update_memory=True)
inputs = tokenizer(input_untokenized, return_tensors='pt', add_special_tokens=False).input_ids.cuda()
outputs = model.generate(input_ids=inputs, max_new_tokens=16)
response = tokenizer.decode(outputs[0][inputs.shape[1]:])
print("response:",response)
# response：
'''sample1:decode=100
import numpy as np
def one_hot_encode(label, dimension):
    label = np.array(label)
    label = np.expand_dims(label, axis=0)
    label = np.eye(dimension)[label]
    return label
</start>
"""
    return result
```

### [2] 代码生成

#### [2.1] 代码生成

> 代码生成

```python
from alchemy.codegen import Codegen
import numpy
import pandas
import numpy as
'''


'''sample2:decode=200
import numpy as np
def one_hot_encode(label, dim):
    """One-hot encode an input label within a given dimension."""
    return np.eye(dim)[label]
</end>
"""
This is an example of a functional description, and you need to write code based on the functional description.
"""
"""
This is an example of a dependency package and version, and you need to write code based on the dependency package and version.
"""
"""
This is an example of a response, and you need to return the code that implements the function.
"""

###Function Description:The function of this code is to print the results predicted by calling the model using vllm.
###dependency and version:vllm==0.3.3
###response:
<start>
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print("Prompt,Generated text")
<end>

###Function Description:This function generates a one-hot encoded array
'''

# 可能需要提供使用样例更好激活？
ctx = """
numpy.zeros(shape, dtype=float, order='C', *, like=None) Return a new array of given shape and type, filled with zeros. 
Examples:
import numpy as np
np.zeros(5)
Above code will return:
array([ 0.,  0.,  0.,  0.,  0.])
"""
# response:This function generates a one-hot encoded array based on the input

# model.inject_memory(tokenizer(ctx, return_tensors='pt', add_special_tokens=False).input_ids.cuda(), update_memory=True)
# inputs = tokenizer(input_untokenized, return_tensors='pt', add_special_tokens=False).input_ids.cuda()
# outputs = model.generate(input_ids=inputs, max_new_tokens=100)
# response = tokenizer.decode(outputs[0][inputs.shape[1]:])
# print("response:",response)
'''sample1
 # You are a professional Python engineer, and I will provide functional descriptions and versions of specified dependency packages.
# You need to write code in Python to implement this feature based on the functional description and using the dependency package and version I specified.
# Please note that you only need to return the code that implements the function, and do not return any other content.
# Please use <start> and <end> to enclose the generated code. Here is an example:
###Function Description:The function of
'''
'''sample2
response: ###Function Description:This function uses the vllm model to generate text based on the input prompt.
###dependency and version:vllm==0.3.3
###response:


###Function Description:This function generates a one-hot encoded array based on the input label within the provided dimension.
###dependency and version:numpy==1.14.3
###response:


###Function Description:This function uses the vllm model to generate text based on the input prompt.
###dependency and
'''

# 可能提问也适应原有训练格式?（是的，对比以上以下结果，确实如此）
# 函数功能描述+使用样例+提问方式
input_untokenized ="""
You are a professional Python engineer, and I will provide functional descriptions and versions of specified dependency packages. \nYou need to write code in Python to implement this feature based on the functional description and using the dependency package and version I specified. \nPlease note that you only need to return the code that implements the function, and do not return any other content. \nPlease use <start> and <end> to enclose the generated code. Here is an example:\n###Function Description:The function of this code is to print the results predicted by calling the model using vllm.\n###dependency and version:vllm==0.3.3\n###response:\n<start>\nfor output in outputs:\n    prompt = output.prompt\n    generated_text = output.outputs[0].text\n    print(\"Prompt,Generated text\")\n<end>\n\nThe Question is as below，generate response according to above format.###Function Description:This function generates a one-hot encoded array based on the input label within the provided dimension.\n###dependency and version:numpy==1.14.3\n###response:\n\n
"""
model.inject_memory(tokenizer(ctx, return_tensors='pt', add_special_tokens=False).input_ids.cuda(), update_memory=True)
inputs = tokenizer(input_untokenized, return_tensors='pt', add_special_tokens=False).input_ids.cuda()
outputs = model.generate(input_ids=inputs, max_new_tokens=100)
response = tokenizer.decode(outputs[0][inputs.shape[1]:])
print("response:",response)

'''sample1
response: ###Function Description:This function generates a one-hot encoded array based on the input label within the provided dimension.
###dependency and version:numpy==1.14.3
###response:


###Function Description:This function generates a one-hot encoded array based on the input label within the provided dimension.
###dependency and version:numpy==1.14.3
###response:


###Function Description:This function generates a one-hot encoded array based on the input label within the provided dimension.
###dependency
'''
# 函数功能描述+提问方式
"""sample1：奇怪的复读机效应，先读了一遍input的example，可能是为了ICL做准备
 ## Answer: 
###Function Description:The function of this code is to print the results predicted by calling the model using vllm.
###dependency and version:vllm==0.3.3
###response:
<start>
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print("Prompt,Generated text")
<end>
"""
'''sample2：decode=200时，复读了5遍，很难绷得住
response: ###Function Description:This function generates a one-hot encoded array based on the input label within the provided dimension.
###dependency and version:numpy==1.14.3
###response:


###Function Description:This function generates a one-hot encoded array based on the input label within the provided dimension.
###dependency and version:numpy==1.14.3
###response:

'''
# 结论:现有prompt可行，只要末尾的dependency没问题（这点还没在这一样例中检验，只在test5samples中检验了），max_length不要太小。但是指令跟随效果一般（对比backbone）


# 猜想2:模型能正确理解需要填充的内容的功能，但是较难直接理解context的source code，除非给定相应的解释。(训练过程中code内容的缺失)

# 猜想3:给定单一有相关性的code context的时候，模型会直接使用；这就意味着，再给定若干个相关的code context时，模型可能无法定位到正确的那一个。