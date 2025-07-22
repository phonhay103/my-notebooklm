from fastapi import FastAPI
from app.api.v1 import users, notebooks, rag

app = FastAPI(title="NotebookLM Clone")

app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(notebooks.router, prefix="/api/v1", tags=["notebooks"])
app.include_router(rag.router, prefix="/api/v1", tags=["rag"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the NotebookLM Clone API"}
