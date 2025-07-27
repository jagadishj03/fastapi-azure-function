import azure.functions as func
from fastapi import Request
from app.main import app
from mangum import Mangum

handler = Mangum(app)

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await handler(req.scope, req.body())
