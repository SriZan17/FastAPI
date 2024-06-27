from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/who2")
def greet2(name: str = Form()):
    return f"Hello, {name}?"
