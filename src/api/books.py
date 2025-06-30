from fastapi import APIRouter, HTTPException
from sqlalchemy import select, delete
from src.api.dependencies import SessionDep, PaginationDep
from src.database import engine, Base
from src.models.books import BookModel
from src.schemas.books import BookGetSchema, BookSchema

router = APIRouter()

@router.post("/setup_database", tags=["База данных"], summary="Создать файл БД")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ok": True}



@router.post("/books", tags=["Книги"], summary="Добавить книгу")
async def add_book(data: BookSchema, session: SessionDep):
    new_book = BookModel(
        title=data.title,
        author=data.author,
    )
    session.add(new_book)
    await session.commit()
    return {"ok": True}



@router.get("/books", tags=["Книги"], summary="Получить все книги")
async def get_books(session: SessionDep, pagination: PaginationDep) -> list[BookGetSchema]:
    query = (
        select(BookModel)
        .limit(pagination.limit)
        .offset(pagination.offset)
    )
    result = await session.execute(query)
    return result.scalars().all()


@router.delete("/books", tags=["Книги"], summary="Удалить книгу")
async def delete_book(book_id: int, session: SessionDep):
    query = delete(BookModel).where(BookModel.id == book_id)
    result = await session.execute(query)
    await session.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Указанная книга не найдена")
    
    return {"msg": "Книга удалена"}