from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.typeScheme import Type, TypeCreate, TypeRead  # Импортируем модели и схемы
from repository.repository import get_db

router = APIRouter()

@router.post("/", response_model=TypeRead)
def create_type(type_create: TypeCreate, db: Session = Depends(get_db)):
    type_instance = Type(**type_create.dict())
    db.add(type_instance)
    db.commit()
    db.refresh(type_instance)
    return type_instance

@router.get("/{type_id}", response_model=TypeRead)
def read_type(type_id: int, db: Session = Depends(get_db)):
    type_instance = db.query(Type).filter(Type.id == type_id).first()
    if type_instance is None:
        raise HTTPException(status_code=404, detail="Type not found")
    return type_instance

@router.get("/", response_model=list[TypeRead])
def read_types(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    types = db.query(Type).offset(skip).limit(limit).all()
    return types
