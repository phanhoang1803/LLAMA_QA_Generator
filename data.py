from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
# from langchain.document_loaders import PyPDFLoader
import pickle
import models

def embed(courseID):
    # loader = PyPDFLoader("/content/data/course1/VietAI_system_research.pdf")
    # docs = loader.load_and_split()

    # Load data from directory
    loader = DirectoryLoader('data/course' + str(courseID), glob="**/*.pdf", loader_cls=PyPDFLoader)
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
    
def embed_and_get_vectorstore(courseID, pdf_path = None):
    # Load data from directory
    if pdf_path == None:
        loader = DirectoryLoader('data/course' + str(courseID), glob="**/*.pdf")
    else:
        loader = PyPDFLoader(file_path=pdf_path)
    docs = loader.load()
    
    # Splitting data into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 20)
    all_splits = text_splitter.split_documents(docs)
    
    # Embedding
    vectorstore = FAISS.from_documents(documents=all_splits, embedding=models.Embeddings.load_embeddings())
    
    return vectorstore

def save_to_json(markdown_text, path):
    import re
    import json
    
    # Extract JSON content from Markdown text
    json_string = re.search(r'```json\n(.*?)```', markdown_text, re.DOTALL).group(1)
    
    # Add comma to separate each group
    json_string = json_string.replace('}\n{', '},\n{')
    
    # Convert JSON string to Python list
    python_list = json.loads(f'[{json_string}]')
    
    # Convert MCQ choices into lists
    for i in python_list:
        i['options'] = i['options'].split('\n')
        
    # Save as json
    with open(path, 'w') as json_file:
        json.dump(python_list, json_file, indent=2)
        
    print("Saved.") 