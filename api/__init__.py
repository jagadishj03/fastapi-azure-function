import azure.functions as func
from fastapi import FastAPI
import logging

app = FastAPI()

@app.get("/api/hello")
async def hello():
    logging.info("/api/hello endpoint was called")
    logging.info("Testing Log")
    return {"message": "Hello from Azure Function"}

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info(f"Azure Function triggered: method={req.method}, url={req.url}")
    # Use AsgiMiddleware directly in the function to ensure correct path handling
    return await func.AsgiMiddleware(app).handle_async(req, context)