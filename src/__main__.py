from llm_sdk import Small_LLM_Model

llm = Small_LLM_Model()
encoded = llm.encode("My name is ")
print(encoded)
