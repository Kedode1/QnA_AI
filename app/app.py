from fastapi import FastAPI, HTTPException, Depends
from app.schemas import DocumentCreate, DocumentResponse
import app.models as models
from uuid import uuid4
from datetime import datetime, timezone
from app.database import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/documents", response_model=list[DocumentResponse])
async def read_all_documents(db: Session = Depends(get_db)):
    documents = db.query(models.Document).all()
    return documents

@app.get("/documents/{document_id}", response_model=DocumentResponse)
async def read_document(document_id: str, db: Session = Depends(get_db)):
    document = db.query(models.Document).filter(models.Document.id == document_id).first()
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@app.post("/documents/", response_model=DocumentResponse, status_code=201)
async def create_document(document: DocumentCreate, db: Session = Depends(get_db)):
    new_document = models.Document(
        id=str(uuid4()),
        title=document.title,
        content=document.content,
        source=document.source,
        created_at=datetime.now(timezone.utc)
    )
    db.add(new_document)
    db.commit()
    db.refresh(new_document)
    return new_document

