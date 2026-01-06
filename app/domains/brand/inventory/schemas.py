from pydantic import BaseModel

class InventoryItem(BaseModel):
    sku: str
    name: str
    quantity: int
