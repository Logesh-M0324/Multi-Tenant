from pydantic import BaseModel

class TenantCreate(BaseModel):
    name: str

class TenantOut(BaseModel):
    id: str
    name: str
    status: str
