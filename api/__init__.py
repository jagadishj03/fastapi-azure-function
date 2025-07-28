import azure.functions as func
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from Azure Function"}

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    # Use AsgiMiddleware directly in the function to ensure correct path handling
    return await func.AsgiMiddleware(app).handle_async(req, context)