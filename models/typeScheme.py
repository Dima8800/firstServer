from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from sqlalchemy.orm import relationship

Base = declarative_base()

class Type(Base):
    __tablename__ = 'types_entity'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

    products = relationship("Product", back_populates="type")

class TypeCreate(BaseModel):
    name: str
    description: str

class TypeRead(BaseModel):
    id: int
    name: str
    description: str