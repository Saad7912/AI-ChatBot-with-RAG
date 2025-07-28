import os
from langchain.document_loaders import PyPDFLoader

def load_all_documents(folder_path: str = "data"):
    loaders = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            loaders.append(PyPDFLoader(os.path.join(folder_path, file)))
    return loaders
