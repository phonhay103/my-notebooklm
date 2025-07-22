from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas

def create_notebook(db: Session, notebook: schemas.NotebookCreate, user_id: int):
    db_notebook = models.Notebook(**notebook.dict(), user_id=user_id)
    db.add(db_notebook)
    db.commit()
    db.refresh(db_notebook)
    return db_notebook

def get_notebooks(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Notebook).filter(models.Notebook.user_id == user_id).offset(skip).limit(limit).all()

def get_notebook(db: Session, notebook_id: int, user_id: int):
    return db.query(models.Notebook).filter(models.Notebook.notebook_id == notebook_id, models.Notebook.user_id == user_id).first()

def add_source_to_notebook(db: Session, source: schemas.SourceCreate, notebook_id: int):
    db_source = models.Source(**source.dict(), notebook_id=notebook_id, status="pending")
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    return db_source
