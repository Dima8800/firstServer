from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, defer
from models.productScheme import Product, ProductCreate, ProductRead
from repository.repository import get_db

router = APIRouter()

@router.get("/", response_model=list[ProductRead])
async def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Product).offset(skip).limit(limit).all()

@router.post("/", response_model=ProductRead)
async def create_product(productDto: ProductCreate, db: Session = Depends(get_db)):
    if productDto.type_id is None:
        return HTTPException(status_code=400, detail="Не указан id типа")

    product = Product(**productDto.dict())

    db.add(product)
    db.commit()
    db.refresh(product)

    return product

@router.get("/{productId}", response_model=ProductRead)
async def read_product(productId: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(productId == Product.id)