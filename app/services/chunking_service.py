from langchain.text_splitter import RecursiveCharacterTextSplitter, SemanticChunker
from langchain.embeddings import HuggingFaceEmbeddings

def chunk_text_recursively(text: str, chunk_size: int = 256, chunk_overlap: int = 50) -> list[str]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""],
    )
    return text_splitter.split_text(text)

def chunk_text_semantically(text: str) -> list[str]:
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    text_splitter = SemanticChunker(embeddings)
    return text_splitter.create_documents([text])
