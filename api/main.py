from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    print("Triggered")
    return {"message": "Deployed from GitHub Actions to Azure Function App"}
