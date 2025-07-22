from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas import schemas
from app.services.rag_service import RAGService
from app.services.vector_store_service import VectorStore
from app.api.v1.notebooks import get_current_user
from app.core.config import DATABASE_URL
import weaviate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_vector_store():
    # This should be configured properly in a real application
    weaviate_url = "http://localhost:8080"
    return VectorStore(weaviate_url)

def get_rag_service(db: Session = Depends(get_db), vector_store: VectorStore = Depends(get_vector_store)):
    return RAGService(db, vector_store)

@router.post("/notebooks/{notebook_id}/chat/", response_model=schemas.ChatResponseSchema)
def chat_with_notebook(
    notebook_id: int,
    query: schemas.ChatQuerySchema,
    rag_service: RAGService = Depends(get_rag_service),
    current_user: schemas.User = Depends(get_current_user),
):
    # In a real app, we would verify the user has access to the notebook
    return rag_service.answer_query(notebook_id, query.query)
