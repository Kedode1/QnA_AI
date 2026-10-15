from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4



class DocumentCreate(BaseModel):
    title: str
    content: str
    source: str = Field(description="The source of the document")


class DocumentResponse(BaseModel):
    id: UUID
    title: str
    content: str
    source: str
    created_at: datetime