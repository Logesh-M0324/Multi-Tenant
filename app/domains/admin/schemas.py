from pydantic import BaseModel

class TenantCreate(BaseModel):
    name: str

class TenantResponse(BaseModel):
    id: str
    name: str
