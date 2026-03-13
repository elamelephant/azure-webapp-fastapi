from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

# API to return the text
@app.get("/", response_class=PlainTextResponse)
async def main():
    return "Welcome to the Demo"

# API to return Hello World text
@app.get("/hello", response_class=PlainTextResponse)
async def hello():
    return "Hello World"

