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
    
    # Alakalı dokümanları alır.
    relevant_docs = retrieve_relevant_docs(collection, query)
    context = "\n---\n".join(relevant_docs) # Bağlamı birleştir
    
    # Sistem promptu, bağlamı ve soruyu birleştirir.
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
    
    # Gemini modelini çağırır.
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=prompt_template
    )
    
    return response.text
