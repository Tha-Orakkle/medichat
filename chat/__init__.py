from core.settings import BASE_DIR
from sentence_transformers import SentenceTransformer

import chromadb
import time
import os



doc_dir = BASE_DIR / 'docs'

# create vector db and document collection

client = chromadb.Client()

doc_collection = client.create_collection("doc_collections")

# create embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# get all document

all_docs = [f for f in os.listdir(doc_dir) if os.path.isfile(os.path.join(doc_dir, f)) and f.endswith('.txt')]


# create document metadata, embedding and add to collection
start_ingestion_time = time.time()
for doc in all_docs:
    doc_data  = {}
    with open(doc_dir / doc, 'r') as file:
        content  = file.readlines()
        doc_data['author'] = content.pop(0).strip()
        doc_data['title'] = content.pop(0).strip()
        doc_data['body'] = ('').join(content)
        embedding = model.encode(doc_data['body'])
        doc_collection.add(
            ids=[doc_data['title']],
            embeddings=[embedding],
            metadatas=[doc_data]
        )
end_ingestion_time = time.time()

ingestion_time = end_ingestion_time - start_ingestion_time
