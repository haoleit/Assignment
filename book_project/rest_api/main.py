import json
import os
from fastapi import FastAPI
import uvicorn
from controller import book_controller

app = FastAPI()

app.include_router(book_controller.router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    