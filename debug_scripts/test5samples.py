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
ctx = """
spacy.load function load a pipeline using the name of an installed package, a string path or a Path-like object. spaCy will try resolving the load argument in this order. If a pipeline is loaded from a string name, spaCy will assume it’s a Python package and import it and call the package’s own load() method. 
"""
input_untokenized = """
You are a professional Python engineer, and I will provide functional descriptions and versions of specified dependency packages. \nYou need to write code in Python to implement this feature based on the functional description and using the dependency package and version I specified. \nPlease note that you only need to return the code that implements the function, and do not return any other content. \nPlease use <start> and <end> to enclose the generated code. Here is an example:\n###Function Description\u951b\u6b55nThe function of this code is to print the results predicted by calling the model using vllm.\n###dependeny and version\u951b\u6b55nvllm==0.3.3\n###response:\n<start>\nfor output in outputs:\n    prompt = output.prompt\n    generated_text = output.outputs[0].text\n    print(\"Prompt,Generated text\")\n<end>\n\n###Function Description\u951b\u6b55nThis Python code reads input from stdin, tokenizes the text using the English language model from the spaCy library, and prints the tokenized words to stdout.\n###dependeny and version\u951b\u6b55n==2.2.3\n###response:\n\n
"""
# please make sure the context to inject into the memory is larger than 16 tokens, this is the hard minimum when training the model. The memory will be disturbed when less than 16 tokens are injected into the memory. 
model.inject_memory(tokenizer(ctx, return_tensors='pt', add_special_tokens=False).input_ids.cuda(), update_memory=True)
inputs = tokenizer(input_untokenized, return_tensors='pt', add_special_tokens=False).input_ids.cuda()
outputs = model.generate(input_ids=inputs, max_new_tokens=100)
response = tokenizer.decode(outputs[0][inputs.shape[1]:])
print("response:",response)
# sample1：decode 100 token
'''
###Function Description锛歕nThis Python code reads input from stdin, tokenizes the text using the English language model from the spaCy library, and prints the tokenized words to stdout.
###dependeny and version锛歕n==2.2.3
###response:
import spacy
import sys
nlp = spacy.load("en_core_web_sm")
for line in sys.stdin:
    doc = nlp(line)
    print(" ".join([token.text
'''
# sample2: decode 200 token,开启复读机模式
'''
response: import sys
import spacy
import json
import sys
import json
'''
# sample3: decode 150 token ,依然复读
'''
response: ###Function Description锛歕nThis Python code reads input from stdin, tokenizes the text using the English language model from the spaCy library, and prints the tokenized words to stdout.
###dependeny and version锛歕n==2.2.3
###response:

###Function Description锛歕nThis Python code reads input from stdin, tokenizes the text using the English language model from the spaCy library, and prints the tokenized words to stdout.
###dependeny and version锛歕n==2.2.3
###response:


###Function Description锛歕nThis Python code reads input from stdin, tokenizes the text using the English language model from the spaCy library
'''
# sample4: decode 100 token,依然复读
'''
response: ###Function Description锛歕nThis Python code reads input from stdin, tokenizes the text using the English language model from the spaCy library, and prints the tokenized words to stdout.
###dependeny and version锛歕n==2.2.3
###response:


###Function Description锛歕nThis Python code reads input from stdin, tokenizes the text using the English language model from the spaCy library, and prints the tokenized words to stdout.
'''
# sample5: 删除最后部分错误编码（猜测spacy==2.2.3的最后提醒很重要，可以激发模型看memory）
input_untokenized = """
You are a professional Python engineer, and I will provide functional descriptions and versions of specified dependency packages. \nYou need to write code in Python to implement this feature based on the functional description and using the dependency package and version I specified. \nPlease note that you only need to return the code that implements the function, and do not return any other content. \nPlease use <start> and <end> to enclose the generated code. Here is an example:\n###Function Description\u951b\u6b55nThe function of this code is to print the results predicted by calling the model using vllm.\n###dependeny and version\u951b\u6b55nvllm==0.3.3\n###response:\n<start>\nfor output in outputs:\n    prompt = output.prompt\n    generated_text = output.outputs[0].text\n    print(\"Prompt,Generated text\")\n<end>\n\n###Function Description\u951b\u6b55nThis Python code reads input from stdin, tokenizes the text using the English language model from the spaCy library, and prints the tokenized words to stdout.\n###dependency and version:spacy==2.2.3\n###response:\n\n
"""
'''
###response:
def tokenize(input):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input)
    return [token.text for token in doc]
if __name__ == "__main__":
'''
# sample5重新采样，依然不报错,可能确实如sample假设所示
'''
response: ###Function Description锛歕nThis Python code reads input from stdin, tokenizes the text using the English language model from the spaCy library, and prints the tokenized words to stdout.
###dependency and version:spacy==2.2.3
###response:
from spacy.lang.en import English
nlp = English()
for line in sys.stdin:
    doc = nlp(line.strip())
    print(" ".join([token.orth_ for token in doc]))
###
'''
# sample5 3次采样，依然不报错,可能确实如sample假设所示
'''
response: ###Function Description锛歕nThis Python code reads input from stdin, tokenizes the text using the English language model from the spaCy library, and prints the tokenized words to stdout.
###dependency and version:spacy==2.2.3
###response:
import spacy
nlp = spacy.load("en_core_web_sm")
text = input()
doc = nlp(text)
for token in doc:
    print(token.text)
```


###Code Output:
``
'''
# Model2:no injection
''' 
response: ###Function Description锛歕nThis Python code reads input from stdin, tokenizes the text using the English language model from the spaCy library, and prints the tokenized words to stdout.
###dependency and version:spacy==2.2.3
###response:
import spacy
import sys
nlp = spacy.load("en_core_web_sm")
for line in sys.stdin:
    doc = nlp(line.strip())
    for token in doc:
        print(token.text
'''
# 总的来看，指令跟随能力依然变差了，无论从test.py还是test5samples.py来看，都存在这个问题
