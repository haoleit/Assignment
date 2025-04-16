import json
import random
import requests

def enrich_books_with_country(input_file, output_file):
   
    try:
      
        response = requests.get("https://restcountries.com/v3.1/all")
        countries = [country["name"]["common"] for country in response.json()]

        
        with open(input_file, "r", encoding="utf-8") as f:
            books = json.load(f)

        # random choice
        for book in books:
            book["publisher_country"] = random.choice(countries)

        # savesave
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(books, f, indent=2, ensure_ascii=False)

        print(f"Successfully enriched book data and saved to {output_file}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    input_file = "../book_project/scraping/books.json"
    output_file = "./api_integration/books_with_country.json"
    enrich_books_with_country(input_file, output_file)
