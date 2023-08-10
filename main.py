from data import DataProcessor

dp = DataProcessor()

dp.embed(1)

# query = "What is the purpose of VietAI organization?"
# docs = db.similarity_search(query)
# print(docs[0].page_content)

# from models import LLAMAModel

# model_id = 'meta-llama/Llama-2-7b-chat-hf'
# hf_auth = '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'

# model = LLAMAModel(model_id, hf_auth)

# chain = model.load_chain(1)

# chat_history = []

# # query = "Please create questions that follow the same structure as Bloom's Taxonomy for each level."
# query = "Please create a set of multiple choice questions that follow the Bloom's Taxonomy and also the correct answer for each question. And for each level, please provide two questions."
# result = chain({"question": query, "chat_history": chat_history})

# print(result['answer'])
