import models
from langchain.chains import ConversationalRetrievalChain

class QA_Generator():
    def __init__(self, model_id, hf_auth):
        self.model_id = model_id
        self.hf_auth = hf_auth
        
    def load_chain(self, courseID):
        # Load llm
        model = models.LLAMAModel(self.model_id, self.hf_auth)
        llm = model.load_llm()
        
        # Load vectorstore that was stored in the disk
        db = data.load_vectorstore(courseID)

        chain = ConversationalRetrievalChain.from_llm(llm, db.as_retriever(), return_source_documents=True)
        return chain

    def query(self, chain, chat_history):
        chat_history = []

        # query = "Please create questions that follow the same structure as Bloom's Taxonomy for each level."
        query = "Please create a set of multiple choice questions that follow the Bloom's Taxonomy and also the correct answer for each question."
        result = chain({"question": query, "chat_history": chat_history})

        return result, chat_history