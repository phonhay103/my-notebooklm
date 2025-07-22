from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    notebooks = relationship("Notebook", back_populates="owner")

class Notebook(Base):
    __tablename__ = "notebooks"

    notebook_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    title = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    owner = relationship("User", back_populates="notebooks")
    sources = relationship("Source", back_populates="notebook")
    chat_history = relationship("ChatHistory", back_populates="notebook")

class Source(Base):
    __tablename__ = "sources"

    source_id = Column(Integer, primary_key=True, index=True)
    notebook_id = Column(Integer, ForeignKey("notebooks.notebook_id"))
    source_type = Column(String, nullable=False)
    original_path_or_url = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    notebook = relationship("Notebook", back_populates="sources")

class ChatHistory(Base):
    __tablename__ = "chat_history"

    message_id = Column(Integer, primary_key=True, index=True)
    notebook_id = Column(Integer, ForeignKey("notebooks.notebook_id"))
    role = Column(String, nullable=False)
    content = Column(String, nullable=False)
    timestamp = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    citations = Column(JSON)

    notebook = relationship("Notebook", back_populates="chat_history")
