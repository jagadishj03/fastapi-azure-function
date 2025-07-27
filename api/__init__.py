from azure.functions import AsgiFunctionApp
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Azure Functions"}

main = AsgiFunctionApp(app)