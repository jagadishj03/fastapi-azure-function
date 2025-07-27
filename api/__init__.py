# api/__init__.py
import azure.functions as func
from fastapi_app.main import app  # adjust import as needed
from mangum import Mangum  # ASGI-to-Azure bridge

handler = Mangum(app)

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return handler(req, context)
