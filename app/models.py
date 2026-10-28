from sqlalchemy import Column, String, DateTime, LargeBinary
from app.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    content = Column(String, nullable=True)
    source = Column(String)
    file_data= Column(LargeBinary, nullable=True)
    created_at = Column(DateTime)
