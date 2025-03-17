# repository.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.typeScheme import Base as TypeBase
from models.productScheme import Base as ProductBase

DATABASE_URL = "postgresql://postgres:passwordBd@localhost:5432/firstPython"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Сначала создаем таблицу Type
    TypeBase.metadata.create_all(bind=engine)
    # Затем создаем таблицу Product
    #ProductBase.metadata.create_all(bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
