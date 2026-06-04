from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Video Editor"}

@app.post("/signup")
def signup():
    return {"message": "User Registered Successfully"}

@app.post("/login")
def login():
    return {"message": "Login Successful"}