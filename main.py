model_id = 'meta-llama/Llama-2-7b-chat-hf'
hf_auth = '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'

# from models import LLAMAModel

# model = LLAMAModel(model_id, hf_auth)
# llm = model.load_llm()

# from QA_Generator import QA_Generator

# qa = QA_Generator(model_id, hf_auth)
# chain = qa.load_chain(llm, 1)

import data

vectorstores = data.embed_and_get_vectorstore(1)