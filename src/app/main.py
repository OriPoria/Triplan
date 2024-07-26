from fastapi import FastAPI, Depends, HTTPException

from src.models.user import User
from src.models.trip import Trip
from src.db.users_db_handler import UsersDbHandler

app = FastAPI()


users_db = UsersDbHandler()

@app.post("/users")
async def create_user(user: User) -> str:
    users_db.create_user(user)
    return "New user added successfully to Triplan systems"


async def create_trip(trip_spec: Trip):
    pass
