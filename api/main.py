from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
def hello_world():
    return JSONResponse(content={"message": "Hello from Azure Function + FastAPI!"})
