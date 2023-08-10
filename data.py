from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
import pickle

import models

class DataProcessor:
    def embed(courseID):
        # loader = PyPDFLoader("/content/data/course1/VietAI_system_research.pdf")
        # docs = loader.load_and_split()

        # Load data from directory
        loader = DirectoryLoader('data/course' + str(courseID), glob="**/*.pdf")
        docs = loader.load()

        # Splitting data into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 20)
        all_splits = text_splitter.split_documents(docs)

        # Embedding
        vectorstore = FAISS.from_documents(documents=all_splits, embedding=models.Embeddings.load_embeddings())

        # Storing
        with open(f"vectorstores/course{str(courseID)}.pkl", "wb") as f:
            pickle.dump(vectorstore, f)

    def load_vectorstore(courseID):
        # Load vectorstore from disk
        with open(f"vectorstores/course{str(courseID)}.pkl", "rb") as f:
            vectorstore = pickle.load(f)

        return vectorstore
    
    def embed_and_get_vectorstore(courseID):
        # Load data from directory
        loader = DirectoryLoader('data/course' + str(courseID), glob="**/*.pdf")
        docs = loader.load()
        
        # Splitting data into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 20)
        all_splits = text_splitter.split_documents(docs)
        
        # Embedding
        vectorstore = FAISS.from_documents(documents=all_splits, embedding=load_embeddings())
        
        return vectorstore