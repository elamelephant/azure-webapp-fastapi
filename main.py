from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

# API to return Hello World text
@app.get("/", response_class=PlainTextResponse)
async def main():
    return "Hello World"
