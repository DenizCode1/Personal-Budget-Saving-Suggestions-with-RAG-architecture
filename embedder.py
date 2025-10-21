import os
from google import genai
from dotenv import load_dotenv

# .env dosyasını yükledim.
load_dotenv() 

# Gemini istemcisini API anahtarı ile başlatır.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_embedding_for_text(text: str) -> list[float]:
    """Gemini'ın text-embedding-004 modelini kullanarak metin için embedding vektörünü oluşturur."""
    
    result = client.models.embed_content(
        model='text-embedding-004',
        contents=[text], # Contents list olarak bekler.
    )
    
    return result.embeddings[0].values 
