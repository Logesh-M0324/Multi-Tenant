from fastapi import APIRouter, Depends
from core.dependencies import get_current_user

router = APIRouter(tags=["User"])

@router.get("/me")
async def me(user=Depends(get_current_user)):
    return user
