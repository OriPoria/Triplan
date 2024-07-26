from datetime import datetime
from pydantic import BaseModel

class Trip(BaseModel):
    start_at: datetime
    end_at: datetime
    destination: str
