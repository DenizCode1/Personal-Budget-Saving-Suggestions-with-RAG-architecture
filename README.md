PERSONAL BUDGET SUGGESTIONS RAG ASSISTANT

🎯 Projenin Amacı 

Bu proje, GenAI Bootcamp kapsamında geliştirilmiş bir RAG (Retrieval Augmented Generation) temelli chatbot projesidir.

Projenin temel amacı kişisel bütçe yönetimi ve finansal tavsiyeler sunmaktır. Proje, Büyük Dil Modellerinin finans gibi spesifik bir alandaki sadece yüklenen onaylanmış finansal dokümanlara dayalı, bağlama uygun ve güvenilir öneriler sunmayı  hedefler.

⚙️ Çözüm Mimarisi

Proje, kişisel finans verilerinden en alakalı bilgiyi alıp, bu bağlamı Gemini modeline besleyen modüler bir RAG zinciri üzerine kurulmuştur.

Generation Model - src/rag_chain.py - Kullanıcının sorusunu ve alınan ilgili bağlamı kullanarak doğal dilde finansal öneri formatında yanıt üretir.
Embedding Model - src/embedder.py - Metin parçalarını vektörlere dönüştürür.
Vector Database - src/indexer.py - Vektörleri saklar ve sorgu sırasında en benzer parçaları bulur.
Data Preprocess - src/ingest.py - Harici makaleleri okur ve kelime / örtüşme ile parçalara ayırır.
RAG Pipeline - src/retriever.py , src/rag_chain.py - Alma ve Üretme süreçlerini yönetir.
Web Interface - src/app.py - Kullanıcı arayüzünü sunar.

📑 Veri Seti Hazırlama

Projede, hazır metin kaynakları kullanılmıştır. Veri seti, kişisel bütçeleme, tasarruf stratejileri, borç yönetimi, emeklilik planlaması, yatırım temelleri ve kredi skoru konularını kapsayan 7 adet makale içeriğinden oluşmaktadır.

Metinler, LLM bağlam limitine uygun hale getirilmek için anlam bütünlüğünü koruyan 500 kelimelik chunk'lara ayrılmıştır.
Önemli bilgilerin kaybolmasını önlemek amacıyla parçalar arasında 100 kelimelik overlap kullanılmıştır.

🚀 Çalışma Kılavuzu

1.Python 3.9 + gereklidir.

2.Klonlama ve Dizin:
git clone https://github.com/DenizCode1/Personal-Budget-Saving-Suggestions-with-RAG-architecture
cd Personal-Budget-Saving-Suggestions-with-RAG-architecture

3.Sanal Ortam Kurulumu:
python -m venv venv
source venv/bin/activate  # macOS/Linux

4.Bağımlılıkların Yüklenmesi:
pip install -r requirements.txt

5.API Anahtarınızı ekleyin ve .env dosyası oluşturun:
GOOGLE_API_KEY=your_api_key

6.Çalıştırma:
streamlit run src/app.py

DEPLOY LİNKİ: https://personal-budget-saving-suggestions-with-rag-architecture-c8vjn.streamlit.app/

<img width="956" height="556" alt="SCR-20251021-uozw" src="https://github.com/user-attachments/assets/8ab6e1ca-23ed-4231-8f77-9bff5494a7ba" />

💻 Kullanılan Teknolojiler:

GenAI : Google Gemini -2.5-Flash

Embedding Model : Google API

Vector Database : ChromaDB

RAG Pipeline : Custom Python Modules

Web Interface : Streamlit

Data Processing : Python, PyPDF2


☎️ İletişim:
denizincece1@gmail.com

GitHub: https://github.com/DenizCode1

LinkedIn: https://www.linkedin.com/in/deniz-ince-8519b0255/


📐 Proje Mimarisi:

personal-budget-suggestions-rag/
├── data/
│   ├── acil_durum_fonu.txt
│   ├── 50_30_20_kurali.txt
│   ├── borc_yonetimi.txt
│   ├── yatirim_temelleri.txt
│   ├── kredi_skoru.txt
│   ├── emeklilik_planlamasi.txt
│   └── zorunlu_tasarruf.txt
├── notebooks/
├── src/
│   ├── app.py             
│   ├── embedder.py        
│   ├── indexer.py         
│   ├── ingest.py          
│   ├── rag_chain.py       
│   └── retriever.py       
├── .gitignore             
├── requirements.txt       
└── README.md              

