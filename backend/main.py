from fastapi import FastAPI

app = FastAPI(title="Industry 4.0 Readiness Console")

@app.get("/")
def root():
    return {"message": "Industry 4.0 Readiness Console API is running"}
