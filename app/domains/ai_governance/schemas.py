from pydantic import BaseModel

class AIDecision(BaseModel):
    decision_id: str
    status: str
