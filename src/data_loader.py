from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader

def load_all_documents(data_dir: str) -> List[Any]:
    """"
    Load all the supported files from the data directories and convert to langchain document structure.
    Supported: PDF, TXT, CSV, DOCX, XLSX, JSON
    """

    data_path = Path(data_dir).resolve()
    print(f"[Debug] Data path: {data_path}")
    documents = []

    pdf_files = list(data_path.glob("**/*.pdf"))
    print(f"[Debug] Found {len(pdf_files)} PDF files: {[str(f) for f in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[Debug] Loading PDF file: {pdf_file}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            loaded = loader.load()
            print(f"[Debug] Loaded {len(loaded)} documents from {pdf_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load PDF {pdf_file}: {e}")


    txt_files = list(data_path.glob("**/*.txt"))
    print(f"[Debug] Found {len(text_files)} TXT files: {[str(f) for f in txt_files]}")
    for txt_file in txt_files:
        print(f"[Debug] Loading TXT file: {txt_file}")
        try:
            loader = TextLoader(str(txt_file))
            loaded = loader.load()
            print(f"[Debug] Loaded {len(loaded)} documents from {txt_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load TXT {txt_file}: {e}")

    
    csv_files = list(data_path.golb("**/*.csv"))
    print(f"[Debug] Found {len(csv_files)} CSV files: {[str(f) for f in csv_files]}")
    for csv_file in csv_files:
        print(f"[Debug] Loading CSV file: {csv_file}")
        try:
            loader = CSVLoader(str(csv_file))
            loaded = loader.load()
            print(f"[Debug] Loaded {len(loaded)} documents from {csv_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load CSV {csv_file}: {e}")


    xlsx_files = list(data_path.glob("**/*.xlsx"))
    print(f"[Debug] Found {len(xlsx_files)} XLSX files: {[str(f) for f in xlsx_files]}")
    for xlsx_file in xlsx_files:
        print(f"[Debug] Loading XLSX file: {xlsx_file}")
        try:
            loader = UnstructuredExcelLoader(str(xlsx_file))
            loaded = loader.load()
            print(f"[Debug] Loaded {len(loaded)} documents from {xlsx_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load XLSX {xlsx_file}: {e}")
    

    docx_files = list(data_path.glob("**/*.docx"))
    print(f"[Debug] Found {len(docx_files)} Docx files: {[str(f) for f in docx_files]}")
    for docx_file in docx_files:
        print(f"[Debug] Loading Dcox_file: {docx_file}")
        try:
            loader = Docx2txtLoader(str(docx_file))
            loaded = loader.load()
            print(f"[Debug] Loaded {len(loaded)} documents from {docx_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to Load Docx {docx_file}: {e}")



    json_files = list(data_path.glob("**/*.json"))
    print(f"[Debug] Found {len(json_files)} JSON files: {[str(f) for f in json_files]}")
    for json_file in json_files:
        print(f"[Debug] Loading JSON file: {json_file}")
        try:
            loader = JSONLoader(str(json_file))
            loaded = loader.load()
            print(f"[Debug] Loaded {len(loaded)} documents from {json_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to Load JSON {json_file}: {e}")


    print(f"[Debug] Total documents loaded: {len(documents)}")
    return documents 


if __name__ == "__main__":
    docs = load_all_documents("../data")
    print(f"Loaded {len(docs)} documents")
    print("Example Documents: ", docs[0] if docs else "Try Adding some Documents in folder")
    
                      