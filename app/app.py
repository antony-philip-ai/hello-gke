from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "Hello from GKE via API Gateway"}
