from fastapi import FastAPI
import uvicorn
from repository.repository import init_db
from controllers.typeController import router as typeRouter

app = FastAPI()

# Инициализация базы данных
init_db()

# Подключаем маршруты контроллеров
app.include_router(typeRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080)
