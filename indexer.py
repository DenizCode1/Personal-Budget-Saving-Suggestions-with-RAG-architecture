import chromadb
from src.embedder import get_embedding_for_text

def build_vector_db(chunks):
    """Metin parçalarını (chunks) ChromaDB'ye ekleyerek vektör veritabanını oluşturur."""
    
    # Varsayılan kalıcı istemci ile veritabanına erişir.
    client = chromadb.Client() 
    # Koleksiyon oluşturma veya mevcutsa alma.
    collection = client.get_or_create_collection("finance_docs") 
    
    # Parçaları döngüye alır, embedding oluşturur.
    for i, chunk in enumerate(chunks):
        # Embedding vektörünü oluştur
        emb = get_embedding_for_text(chunk)
        
        # ChromaDB'ye ekler.
        collection.add(
            ids=[f"doc_{i}"], # Her parça için benzersiz ID oluşturur.
            documents=[chunk],
            embeddings=[emb],
        )
    print(f"Toplam {len(chunks)} parça ChromaDB'ye başarıyla indexlendi.")
    return collection
