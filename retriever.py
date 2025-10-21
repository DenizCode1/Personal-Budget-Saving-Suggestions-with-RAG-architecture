from src.embedder import get_embedding_for_text
import chromadb

def retrieve_relevant_docs(collection: chromadb.Collection, query: str, n_results: int = 3) -> list[str]:
    """Kullanıcı sorgusuna en alakalı dokümanları vektör veritabanından alır."""
    
    # Sorgu metnini embeddinge dönüştürür
    query_embedding = get_embedding_for_text(query) # Bu fonksiyon şimdi tek bir embeddingi döndürüyor

    # Vektör veritabanında arama yapar.
    results = collection.query(
        query_embeddings=[query_embedding], 
        n_results=n_results
    )
    
    # Alınan doküman metinlerini döndürür.
    retrieved_documents = results.get('documents')[0] if results.get('documents') else []
    
    return retrieved_documents
