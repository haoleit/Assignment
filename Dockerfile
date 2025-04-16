FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY book_project /app/book_project

# Set environment variables
ENV API_KEY=authenticate_api_key

# Change directory to `book_project/rest_api` and run `uvicorn main:app`
WORKDIR /app/book_project/rest_api

# Run the Uvicorn server
CMD ["python", "main.py" ]
