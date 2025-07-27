import azure.functions as func
from api.main import app

main = func.AsgiFunctionApp(app=app)