import os
from google import genai
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv() 

# Gemini istemcisini API anahtarı ile başlat
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_embedding_for_text(text: str) -> list[float]:
    """Gemini'ın text-embedding-004 modelini kullanarak metin için embedding vektörünü oluşturur."""
    
    result = client.models.embed_content(
        model='text-embedding-004',
        contents=[text], # Contents list olarak bekler
    )
    
    # KESİN HATA DÜZELTME:
    # 1. result.embeddings[0] bize bir ContentEmbedding nesnesi verir.
    # 2. ChromaDB'nin istediği saf float listesine erişmek için bu nesnenin `.values` özelliğini kullanmalıyız.
    return result.embeddings[0].values # <-- BU SATIR YENİDEN VE KESİN OLARAK GÜNCELLENDİ