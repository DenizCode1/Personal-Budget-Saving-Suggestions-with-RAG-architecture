import streamlit as st
import os
from dotenv import load_dotenv

# Path sorununu çözmek için ana dizini PATH'e ekledim.
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Kendi modüllerimi import ediyorum.
from src.ingest import chunk_text, load_text_files, load_pdfs
from src.indexer import build_vector_db
from src.rag_chain import answer_query
import chromadb

load_dotenv() 

# Veri setini bir kere yükleyip indexlemek için Streamlit cache kullandım.
# Bu, her yenilemede indexleme işleminin tekrar yapılmasını önlüyor.
@st.cache_resource 
def process_and_index_data(folder_path="./data"):
    # TXT ve PDF dosyalarını yükler.
    all_docs = load_text_files(folder_path) + load_pdfs(folder_path)
    
    if not all_docs:
        st.error("Data klasöründe hiç veri bulunamadı. Lütfen data/ klasörüne .txt veya .pdf dosyası ekleyin.")
        return None

    # Tüm metinleri birleştirir ve chunk'lar
    full_text = "\n\n".join([doc["text"] for doc in all_docs])
    chunks = chunk_text(full_text)
    
    # ChromaDB'yi oluşturur.
    collection = build_vector_db(chunks)
    return collection

# Ana Streamlit uygulaması
st.title("💰 Personal Budget Suggestions RAG Asistanı (Gemini)")
st.markdown("---")

# Veri Yükleme ve Indexleme 
collection = process_and_index_data()

if collection:
    st.success(f"✅ Bütçe ve finansal veri kaynaklarınız ('data/' klasöründen) başarıyla yüklendi ve indexlendi.")

    # Kullanıcı Sorgusu
    query = st.text_input("Bütçeniz, tasarruflarınız veya borçlarınız hakkında bir soru sorun:", 
                          placeholder="Örneğin: Borç yönetimi için Kartopu yöntemi ne zaman daha iyi bir stratejidir?")

    if st.button("💡 Öneri Al (RAG Sorgusu)"):
        if query:
            with st.spinner("Yanıt oluşturuluyor... (Retrieval ve Gemini Generation)"):
                # RAG zincirini çalıştırıyor.
                answer = answer_query(query, collection)
            
            st.markdown("---")
            st.markdown("### 💬 **Asistan Yanıtı**")
            st.write(answer)
        else:
            st.warning("Lütfen asistanın yanıtlaması için bir soru girin.")
