from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
import data.creature as creature
import data.explorer as explorer

app = FastAPI()
top = Path(__file__).resolve().parent
template_obj = Jinja2Templates(directory=f"{top}/template")


@app.get("/list")
def explorer_list(request: Request):
    return template_obj.TemplateResponse(
        "list.html",
        {
            "request": request,
            "explorers": explorer.get_all(),
            "creatures": creature.get_all(),
        },
    )


if __name__ == "__main__":
    uvicorn.run("template:app", reload=True)
