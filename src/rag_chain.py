import os
from google import genai
from src.retriever import retrieve_relevant_docs
from dotenv import load_dotenv
import chromadb

load_dotenv()
# Gemini istemcisini başlat
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def answer_query(query: str, collection: chromadb.Collection) -> str:
    """RAG mimarisi kullanarak bir sorguyu yanıtlar (Retrieval + Generation)."""
    
    # 1. Retrieval (Alma) Adımı: Alakalı dokümanları al
    relevant_docs = retrieve_relevant_docs(collection, query)
    context = "\n---\n".join(relevant_docs) # Bağlamı birleştir
    
    # 2. Prompt Oluşturma Adımı: Sistem prompt'u, bağlamı ve soruyu birleştir
    prompt_template = f"""
    Sen kişisel bütçe yönetimi ve tasarruf önerileri sunan bir yapay zeka asistanısın. Görevin, SADECE aşağıda verilen 'Bağlam (Context)' içinde yer alan bilgilere dayanarak kullanıcının sorusunu yanıtlamaktır.
    Eğer bağlamda soruya cevap verecek yeterli bilgi yoksa, 'Üzgünüm, bu konu hakkında elimde yeterli bilgi yok.' diye yanıt ver.
    Yanıtın kısa, net ve finansal öneri formatında olsun.
    
    Bağlam (Context):
    ---
    {context}
    ---
    
    Kullanıcı Sorusu: {query}
    """
    
    # 3. Generation (Üretim) Adımı: Gemini modelini çağır
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=prompt_template
    )
    
    return response.text