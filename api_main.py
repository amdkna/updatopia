# api_main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from engine.db import init_db, get_player, update_player
from engine.rules import calc_level

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    init_db()

@app.get("/state")
async def get_state():
    player = get_player()
    total_xp = player.dept_xp + player.n_xp
    return {
        "player": {
            "id": player.id,
            "name": player.name,
            "dept_coins": player.dept_coins,
            "dept_xp": player.dept_xp,
            "n_coins": player.n_coins,
            "n_xp": player.n_xp,
            "level": calc_level(total_xp),
            "total_xp": total_xp,
        }
    }

class Event(BaseModel):
    type: str         # e.g. "learning_minute", "work_minute"
    timestamp: str    # ISO-8601 string

@app.post("/event")
async def post_event(evt: Event):
    # rudimentary validation
    if evt.type not in ("learning_minute", "work_minute"):
        raise HTTPException(400, "Unsupported event type")

    player = get_player()
    if evt.type == "learning_minute":
        # +1 dept coin & dept XP
        player.dept_coins += 1
        player.dept_xp   += 1
    else:  # work_minute
        player.n_coins += 1
        player.n_xp    += 1

    update_player(player)
    total_xp = player.dept_xp + player.n_xp
    return {"level": calc_level(total_xp), "total_xp": total_xp}
