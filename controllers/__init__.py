from fastapi import APIRouter

# Импортируем маршруты из контроллеров
from .typeController import router as typeRouter
from .productController import router as productRouter

# Создаем основной маршрутизатор
router = APIRouter()

# Включаем маршруты в основной маршрутизатор
router.include_router(typeRouter, prefix="/types", tags=["types"])
router.include_router(productRouter, prefix="/products", tags=["products"])