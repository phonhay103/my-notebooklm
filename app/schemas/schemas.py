from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class NotebookBase(BaseModel):
    title: str

class NotebookCreate(NotebookBase):
    pass

class Notebook(NotebookBase):
    notebook_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class SourceBase(BaseModel):
    source_type: str
    original_path_or_url: str

class SourceCreate(SourceBase):
    pass

class Source(SourceBase):
    source_id: int
    notebook_id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True

class ChatHistoryBase(BaseModel):
    role: str
    content: str
    citations: Optional[List[str]] = None

class ChatHistoryCreate(ChatHistoryBase):
    pass

class ChatHistory(ChatHistoryBase):
    message_id: int
    notebook_id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
