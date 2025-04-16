from pydantic import BaseModel

class BookDTO(BaseModel):
    title: str
    price: float
    availability: str
    product_page: str
    star_rating: int
    publisher_country: str
