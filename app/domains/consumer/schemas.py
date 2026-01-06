from pydantic import BaseModel

class ConsumerProfile(BaseModel):
    preferences: dict = {}
