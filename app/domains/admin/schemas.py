from pydantic import BaseModel

class TenantCreate(BaseModel):
    name: str
    status: str = "ACTIVE"
    
class TenantUpdate(BaseModel):
    status: str

class TenantResponse(BaseModel):
    id: str
    name: str
