from fastapi import APIRouter

router = APIRouter(
    prefix="/brand/policies",
    tags=["Brand Policies"]
)

@router.get("/")
async def list_policies():
    return []
