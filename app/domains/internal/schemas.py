from pydantic import BaseModel

class InternalAuthRequest(BaseModel):
    token: str
