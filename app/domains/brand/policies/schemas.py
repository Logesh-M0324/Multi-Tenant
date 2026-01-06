from pydantic import BaseModel

class Policy(BaseModel):
    name: str
    rules: dict
