from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import pandas as pd
import os

df = pd.read_csv("email_list.csv")
embeding = OllamaEmbeddings(model="embeddinggemma")

db_local = "./chrome.db"
add_document = not os.path.exists(db_local)

if add_document:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content = row["Pytanie"] + " " + row["Odp"],
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store =Chroma(
    collection_name="email_list",
    persist_directory=db_local,
    embedding_function=embeding
)

if add_document:
    vector_store.add_documents(documents=documents, ids = ids)

retriever = vector_store.as_retriever(
    search_kwargs = {"k":5}
)