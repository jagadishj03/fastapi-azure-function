import azure.functions as func
from .api import app

main = func.AsgiFunctionApp(app=app)