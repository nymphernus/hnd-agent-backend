from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    title: str
    author: str

class BookGetSchema(BaseModel):
    id: int
    title: str
    author: str

class PaginationParams(BaseModel):
    limit: int = Field(5, ge=0, le=100, description="Кол-во элементов на странице")
    offset: int = Field(0, ge=0, description="Смещение")