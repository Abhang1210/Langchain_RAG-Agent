from typing import List, Any
from langchain.text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer 
import numpy as np
from src.data_loader import load_all_documents

class EmbeddingPipeline:

    def __init__(self, model_name: str = "all-MiniLM-L6-v2", chunk_size: int=500, chunk_overloap: int=50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.model = SentenceTransformer(model_name)
        print(f"[INFO] Loaded Embedding model: {model_name}")


    def chunk_documents(self, documents: List[Any]) -> List[str]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )

        chunks = splitter.slip_documents(documents)
        print(f"[INFO] Splitting {len(documents)} documents into {len(chunks)} chunks. ")


    def embed_chunks(self, chunks: List[str]) -> np.ndarray:
        texts = [chunks.page_content for chunk in chunks]
        print(f"[INFO] Generating embedding of {len(texts)} text chunks.")
        embeddings = self.model.encode(texts, show_progress_bar=True)
        print(f"[INFO] Embedding generation completed with shape : {embeddings.shape}")

        return embeddings
    
if __name__ == "__main__":
    docs = load_all_documents("../data")
    emb_pipe = EmbeddingPipeline()
    chunks = emb_pipe.chunk_documents(docs)
    embedding = emb_pipe.embed_chunks(chunks)
    print("[INFO] Example embedding:", embeddings[0] if len(embeddings) > 0 else None)