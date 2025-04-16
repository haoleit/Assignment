# Book Project

This project consists of three parts: web scraping, API integration, and building a REST API.

## Part 1: Web Scraping

- The scraping scripts are located in the `scraping/` directory.
- To run the scraping script, navigate to the `scraping/` directory and run `python scraper.py`.
- The scraped data will be saved in `books.json` or `books.csv`.
- The raw HTML of each product page will be saved in the `html_backup/` directory.

## Part 2: API Integration

- The API integration scripts are located in the `api_integration/` directory.
- To run the API integration script, navigate to the `api_integration/` directory and run `python api_integration.py`.
- The updated data will be saved in `books_with_country.json` or `books_with_country.csv`.

## Part 3: REST API

- The REST API code is located in the `rest_api/` directory.
- To run the REST API, navigate to the `rest_api/` directory and run `python main.py`.
- The API will be available at `http://localhost:8000`.

## Bonus (Optional)

- Caching for the REST Countries API
- API limitation by header authorization
- Logging and exception handling
- Dockerizing the entire project
- Writing unit tests for the API endpoints

## Submission Requirements

- The full source code (via GitHub or zip file)
- Instructions on how to run the code and API (README.md)
- The output data files:
  - books.json or books.csv
  - books_with_country.json or .csv
- The `html_backup/` folder containing the raw HTML files
- (If applicable) Dockerfile and docker-compose.yml
- (If applicable) Unit tests and instructions to run them
