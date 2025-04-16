import json

from functools import lru_cache
from typing import List
from dto import BookDTO

class BookService:
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.books: List[BookDTO] = self._load_books()

    def _load_books(self) -> List[BookDTO]:
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                books_data = json.load(f)
            return [BookDTO(**book) for book in books_data]
        except FileNotFoundError:
            return []
    # @lru_cache(maxsize=128)
    def get_books(self, country: str = None) -> List[BookDTO]:
        if country:
            return [book for book in self.books if book.publisher_country == country]
        return self.books

    def add_book(self, book: BookDTO):
        self.books.append(book)
        self._save_books()
        self.reload_books()

    def delete_book(self, title: str):
        initial_len = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        if len(self.books) == initial_len:
            raise ValueError("Book not found")
        self._save_books()
        self.reload_books()

    def _save_books(self):
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump([book.dict() for book in self.books], f, indent=2, ensure_ascii=False)
    def reload_books(self):
        
        self.books = self._load_books()


