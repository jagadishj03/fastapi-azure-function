import azure.functions as func
from fastapi.middleware.wsgi import WSGIMiddleware
from .api import app

main = func.AsgiFunctionApp(app=WSGIMiddleware(app))
