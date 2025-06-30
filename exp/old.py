from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()


books = [
    {
        "id": 1,
        "title": "Первая книга",
        "author": "Писатель 1",
    },
    {
        "id": 2,
        "title": "Вторая книга",
        "author": "Писатель 2",
    },
]

@app.get("/booksold", tags=["КнигиОлд"], summary="Получить все книги")
def read_books():
    return books

@app.get("/booksold/{id}", tags=["КнигиОлд"], summary="Получить определенную книгу")
def get_book(id: int):
    for book in books:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

class NewBook(BaseModel):
    title: str
    author: str

@app.post("/booksold", tags=["КнигиОлд"], summary="Добавить книгу")
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author,
    })
    return {"success": True, "message": "Книга добавлена"}

data = {
    "email": "abc@mail.ru",
    "bio": "бабабуй123",
    "age": 12,
}

data_wo_age = {
    "email": "abc@mail.ru",
    "bio": "бабабуй123"
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)

    model_config = ConfigDict(extra='forbid')

users = []

@app.post("/users", tags=["Пользователи"], summary="Добавить пользователя")
def add_user(user: UserSchema):
    users.append(user)
    return {"succ": True, "msg": "Пользователь добавлен"}

@app.get("/users", tags=["Пользователи"], summary="Отобразить пользователей")
def get_user() -> list[UserSchema]:
    return users



class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)


# print(repr(UserSchema(**data_wo_age)))
# print(repr(UserAgeSchema(**data)))






















if __name__ == "__main__":
    uvicorn.run("old:app", reload=True)