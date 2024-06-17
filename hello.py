from fastapi import FastAPI, Body, Header, Response

app = FastAPI()


@app.get("/hi")
def greet(who):
    return f"Hello {who}"


@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return f"normal {name} body {value}"


@app.post("/ho")
def greeto(who: str = Header):
    return f"Hello? {who}"


@app.get("/happy")
def happy(status_code=200):
    return ":)"


@app.post("/agent")
def get_agent(user_agent: str = Header()):
    return user_agent


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("hello:app", reload=True)
