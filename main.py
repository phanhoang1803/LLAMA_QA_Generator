model_id = 'meta-llama/Llama-2-7b-chat-hf'
hf_auth = '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'

# from models import LLAMAModel

# model = LLAMAModel(model_id, hf_auth)
# llm = model.load_llm()

# from QA_Generator import QA_Generator

# qa = QA_Generator(model_id, hf_auth)
# chain = qa.load_chain(llm, 1)

import data
import QA_Generator 
from langchain.llms import OpenAI

import os
os.environ["OPENAI_API_KEY"] = "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"


# from models import LLAMAModel

# llama = LLAMAModel(model_id, hf_auth)
# llm = llama.load_llm(temperature=0.5, max_new_tokens=1024)

chain = QA_Generator.load_chain(llm=OpenAI(), courseID=1, pdf_path="data\course1\VietAI_system_research.pdf")

chat_history = []

# query = "Please create questions that follow the same structure as Bloom's Taxonomy for each level."
query = "Please create a set of multiple choice questions that follow the Bloom's Taxonomy and also the correct answer for each question. And for each level, please provide two questions."
result = chain({"question": query, "chat_history": chat_history})

print(result['answer'])