from fastapi import FastAPI

app = FastAPI(title="AI Video Editor API")

@app.get("/")
def root():
    return {"message": "AI Video Editor backend is running"}