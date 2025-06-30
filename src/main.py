from fastapi import FastAPI, Request, Response
import uvicorn
from src.api import main_router
from fastapi.middleware.cors import CORSMiddleware
import time
from typing import Callable

app = FastAPI()
app.include_router(main_router)


# Настройка CORS
origins = [
    "http://localhost:5022",  # Сюда поставьте URL вашего фронтенда
    "http://127.0.0.1:5022",  # и другие адреса, с которых приходят запросы
]
# Связь с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Разрешите все методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"],  # Разрешите все заголовки
)



# @app.middleware("http")
# async def my_middleware(request: Request, call_next: Callable):
#     ip_address = request.client.host
#     # if ip_address in ["127.0.0.2", "localhostz"]:
#     #     return Response(status_code=429, content="Превышено количество запросов")
#     start = time.perf_counter()
#     response = await call_next(request)
#     end = time.perf_counter() - start
#     print(end, ip_address)
#     response.headers["X-Special"] = "dopolnitelnyay informatia na angl only"
#     return response


if __name__ == "__main__":
    uvicorn.run("mian:app", reload=True)