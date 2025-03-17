from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pydantic import BaseModel

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'  # Исправлено

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Integer)

    type_id = Column(Integer, ForeignKey('types_entity.id'))
    type = relationship("Type", back_populates="products")

class ProductCreate(BaseModel):
    name: str
    description: str
    price: int
    type_id: int

class ProductRead(BaseModel):
    id: int
    name: str
    description: str
    type_id: int