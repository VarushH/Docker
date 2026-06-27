from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "API Running"}

@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello {name}! Welcome to Docker + Streamlit."
    }