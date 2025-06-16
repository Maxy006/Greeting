from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Greeting API!"}

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}! Have a great day!"}
