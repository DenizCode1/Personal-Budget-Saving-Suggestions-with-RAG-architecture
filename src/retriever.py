from src.embedder import get_embedding_for_text
import chromadb

def retrieve_relevant_docs(collection: chromadb.Collection, query: str, n_results: int = 3) -> list[str]:
    """Kullanıcı sorgusuna en alakalı dokümanları vektör veritabanından alır."""
    
    # 1. Sorgu metnini embedding'e dönüştür
    query_embedding = get_embedding_for_text(query) # Bu fonksiyon şimdi tek bir embedding döndürüyor

    # 2. Vektör veritabanında arama yap (k-Nearest Neighbors - kNN)
    results = collection.query(
        query_embeddings=[query_embedding], # <-- BU SATIR GÜNCELLENDİ: Embedding listesini bekliyor
        n_results=n_results
    )
    
    # Alınan doküman metinlerini döndür
    retrieved_documents = results.get('documents')[0] if results.get('documents') else []
    
    return retrieved_documents