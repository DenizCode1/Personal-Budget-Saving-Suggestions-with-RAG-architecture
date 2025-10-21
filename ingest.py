import PyPDF2
from pathlib import Path

def load_text_files(folder_path):
    """Klasördeki tüm TXT dosyalarını yükler."""
    texts = []
    # Klasördeki tüm .txt dosyalarını bulur
    for file in Path(folder_path).glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            texts.append({"source": str(file), "text": f.read()})
    return texts

def load_pdfs(folder_path):
    """Klasördeki tüm PDF dosyalarını yükler."""
    texts = []
    for file in Path(folder_path).glob("*.pdf"):
        try:
            reader = PyPDF2.PdfReader(file)
            pages_text = []
            for page in reader.pages:
                p_text = page.extract_text()
                if p_text:
                    pages_text.append(p_text)
            
            # Tüm sayfaları tek bir metinde birleştir
            text = "\n".join(pages_text)
            texts.append({"source": str(file), "text": text})
        except Exception as e:
            print(f"Hata oluştu: {file}: {e}")
            
    return texts

def chunk_text(text: str, chunk_size=500, overlap=100):
    """
    Basit kelime bazlı metin parçalama (chunking) yapar.
    
    chunk_size: bir chunk'taki kelime sayısı (500 kelime)
    overlap: chunk'lar arasındaki örtüşme (100 kelime)
    """
    words = text.split()
    chunks = []
    
    # Parçalama işlemini örtüşme ile gerçekleştirir
    for i in range(0, len(words), chunk_size - overlap):
        chunk_words = words[i:i + chunk_size]
        chunk = " ".join(chunk_words)
        chunks.append(chunk)
        
    return chunks