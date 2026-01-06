from pydantic import BaseModel

class UHNIProfile(BaseModel):
    preferences: dict = {}
