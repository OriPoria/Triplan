from fastapi import FastAPI

from src.models.trip import Trip

app = FastAPI()


async def get_trip(input_prompt) -> Trip:
    pass
