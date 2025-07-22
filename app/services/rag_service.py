from app.services.vector_store_service import VectorStore
from app.services.ingestion_service import extract_text_from_url, extract_text_from_pdf, extract_text_from_docx
from app.services.chunking_service import chunk_text_recursively
from app.models import models
from sqlalchemy.orm import Session

class RAGService:
    def __init__(self, db: Session, vector_store: VectorStore):
        self.db = db
        self.vector_store = vector_store

    def process_source(self, source: models.Source):
        if source.source_type == "url":
            text = extract_text_from_url(source.original_path_or_url)
        elif source.source_type == "pdf":
            text = extract_text_from_pdf(source.original_path_or_url)
        elif source.source_type == "docx":
            text = extract_text_from_docx(source.original_path_or_url)
        else:
            raise ValueError(f"Unsupported source type: {source.source_type}")

        chunks = chunk_text_recursively(text)
        self.vector_store.add_chunks(chunks, source.source_id, source.notebook_id)
        source.status = "processed"
        self.db.commit()

    def answer_query(self, notebook_id: int, query: str):
        # This is a placeholder for the generation part of the RAG pipeline.
        # In a real implementation, this would involve a call to a large language model.
        context = self.vector_store.search(query, notebook_id)
        response = f"Query: {query}\n\nContext:\n"
        for item in context:
            response += f"- {item['content']} (Source ID: {item['source_id']})\n"
        return {"response": response, "citations": [item['source_id'] for item in context]}
