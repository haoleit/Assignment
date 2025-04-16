from fastapi import APIRouter, HTTPException, Query, Header,Request
from typing import List, Optional
from service import BookService
from dto import BookDTO
import functools
import os

API_KEY = os.environ.get("API_KEY", "authenticate_api_key")


def require_api_key(func):
    @functools.wraps(func)
    async def wrapper(*args, request: Request= None, **kwargs):
        api_key=request.headers.get('api_key')
        if api_key != API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API Key")
        return await func(*args, **kwargs)
    return wrapper

router = APIRouter()
book_service = BookService("../api_integration/books_with_country.json")

@router.get("/books",response_model=List[BookDTO])
@require_api_key
async def get_books(country: Optional[str] = Query(None),request: Request= None):
    
    return book_service.get_books(country)

@router.post("/books", response_model=BookDTO)
@require_api_key
async def create_book(book: BookDTO,request: Request= None):
   
    book_service.add_book(book)
    return book

@router.delete("/books/{title}")
@require_api_key
async def delete_book(title: str,request: Request= None):
   
    try:
        book_service.delete_book(title)
        return {"message": f"Book '{title}' deleted successfully"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Book not found")
