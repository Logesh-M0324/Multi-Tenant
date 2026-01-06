from pydantic import BaseModel

class UserProfile(BaseModel):
    email: str
    role: str
