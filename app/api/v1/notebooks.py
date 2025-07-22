from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import SessionLocal
from app.schemas import schemas
from app.services import notebook_service, user_service
from app.api.v1.users import get_db
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verify_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    email = verify_token(token, credentials_exception)
    user = user_service.get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user

@router.post("/notebooks/", response_model=schemas.Notebook)
def create_notebook(
    notebook: schemas.NotebookCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    return notebook_service.create_notebook(db=db, notebook=notebook, user_id=current_user.user_id)

@router.get("/notebooks/", response_model=List[schemas.Notebook])
def read_notebooks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    notebooks = notebook_service.get_notebooks(db, user_id=current_user.user_id, skip=skip, limit=limit)
    return notebooks

@router.get("/notebooks/{notebook_id}", response_model=schemas.Notebook)
def read_notebook(
    notebook_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    db_notebook = notebook_service.get_notebook(db, notebook_id=notebook_id, user_id=current_user.user_id)
    if db_notebook is None:
        raise HTTPException(status_code=404, detail="Notebook not found")
    return db_notebook

@router.post("/notebooks/{notebook_id}/sources/", response_model=schemas.Source)
def add_source_to_notebook(
    notebook_id: int,
    source: schemas.SourceCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    db_notebook = notebook_service.get_notebook(db, notebook_id=notebook_id, user_id=current_user.user_id)
    if db_notebook is None:
        raise HTTPException(status_code=404, detail="Notebook not found")
    return notebook_service.add_source_to_notebook(db=db, source=source, notebook_id=notebook_id)
