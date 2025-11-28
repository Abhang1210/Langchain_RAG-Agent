import os
import faiss
import numpy as np
from typing import List, Any
from sentence_transformers import SentenceTransformer 
from src.embedding import EmbeddingPipeline


class FaissVectorStore:

    def __init__(self, persist_dir: str = "faiss_store", embedding_model: str = "all-MiniLM-L6-v2", chunk_size: int =1000, chunk_overlap: int = 100):
        self.persist_dir = persist_dir
        os.makedirs(self.persist_dir, exist_ok=True)
        self.index=None
        self.metadata = []
        self.embedding_model = embedding_model
        self.model = SentenceTranssformer(embedding_model)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        print(f"[INFO] Initialize the Embedding Model: {embedding_model}")


    def build_from_documents(self, documents: List[Any]):
        print(f"[INFO] Building Vector Store from {len(documents)} raw Documents.")
        embedding_pipeline = EmbeddingPipeline(model_name=self.embedding_model, chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        chunks = embedding_pipeline.chunk_documents(documents)
        embedding = embedding_pipeline.embed_chunks(chunks)
        metadata = [{"text": chunk.page_content} for chunk in chunks]
        self.add_embeddings(np.array(embedding).astype("float32"), metadata)
        self.save()
        print(f"[INFO] Vector Store built and saved to {self.persist_dir}")

    def add_embeddings(self, embeddings: np.ndarray, metadata: List[Any]=None):
        dimension = embeddings.shape[1]
        if self.index is None:
            self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)
        if metadata:
            self.metadata.extend(metadata)
        print(f"[INFO] Added {embeddings.shape[0]} vectors to Faiss Index")

    def save(self):
        faiss_path = os.path.join(self.persist_dir, "faiss.index")