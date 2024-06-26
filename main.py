import uvicorn
from fastapi import FastAPI

# from web import explorer, creature, user, game
from web import explorer, creature, game

app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)
# app.include_router(user.router)
app.include_router(game.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
