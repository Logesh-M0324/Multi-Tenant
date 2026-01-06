from fastapi import APIRouter, Depends, HTTPException
from domains.auth.schemas import SignUpRequest, LoginRequest, TokenResponse
from domains.auth.service import AuthService
from core.database import get_db


router = APIRouter(prefix="/auth", tags=["Auth"])

# ----------------------------
# Sign Up
# ----------------------------
@router.post("/signup", response_model=TokenResponse)
async def sign_up(payload: SignUpRequest, db = Depends(get_db)):
    try:
        service = AuthService(database=db)
        print(service)
        user = await service.sign_up(
            email=payload.email,
            password=payload.password,
            tenant_id=payload.tenant_id,
            role=payload.role
        )
        print(user)
        token = await service.login(payload.email, payload.password)
        print(token)
        return token
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ----------------------------
# Login
# ----------------------------
@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest, db = Depends(get_db)):
    try:
        service = AuthService(database=db)
        return await service.login(payload.email, payload.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

# ----------------------------
# Logout
# ----------------------------
@router.post("/logout")
async def logout():
    """
    In a real enterprise zero-trust system, token revocation would require:
    - Redis blacklist
    - Short-lived JWTs
    For MVP, we just return OK
    """
    return {"status": "logged out"}
