from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Union
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Union[int, None] = None
    title: str = Field(min_length=3, description="The title of the book")
    author: str = Field(min_length=1, description="The author of the book")
    description: str = Field(min_length=1,
                             description="The description of the book")
    rating: int = Field(ge=1, le=5, description="The rating of the book")
    published_date: int = Field(gt=1999,
                                lt=2030,
                                description="The published date of the book")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Title One",
                "author": "Author One",
                "description": "Description One",
                "rating": 4,
                "published_date": 2020
            }
        }


BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby", "A very nice book!", 5,
         2030),
    Book(2, "Be Fast with FastAPI", "codingwithroby", "A great book!", 5,
         2030),
    Book(3, "Master Endpoints", "codingwithroby", "A awesome book!", 5, 2029),
    Book(4, "HP1", "Author 1", "Book Description", 2, 2028),
    Book(5, "HP2", "Author 2", "Book Description", 3, 2027),
    Book(6, "HP3", "Author 3", "Book Description", 1, 2026)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/book/{book_id}", status_code=status.HTTP_200_OK)
async def read_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_books_by_rating(rating: int = Query(gt=0, lt=6)):
    books_with_given_rating = [book for book in BOOKS if book.rating == rating]
    if not books_with_given_rating:
        return {"message": "No books found with the given rating"}
    return books_with_given_rating


@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    return BOOKS


@app.put("/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_request: BookRequest):
    updated_book = Book(**book_request.model_dump())
    for index, book in enumerate(BOOKS):
        if book.id == updated_book.id:
            BOOKS[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/delete_book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    for index, book in enumerate(BOOKS):
        if book.id == book_id:
            BOOKS.pop(index)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")


def find_book_id(book: Book) -> Book:
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book