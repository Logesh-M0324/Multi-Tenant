from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from domains.auth.schemas import SignUpRequest, LoginRequest, TokenResponse
from domains.auth.service import AuthService
from core.database import get_db
from core.dependencies import get_current_user,auth_scheme #oauth2_scheme,
from core.token_blacklist import TokenBlacklist
from jose import jwt
from core.config import settings

router = APIRouter(prefix="/auth", tags=["Auth"])

#auth_scheme = HTTPBearer()

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
        print("service in login", service)
        return await service.login(payload.email, payload.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

# ----------------------------
# Logout
# ----------------------------
 
@router.post("/logout") 
async def logout( token: HTTPAuthorizationCredentials = Depends(auth_scheme), user = Depends(get_current_user) ):
    try: 
        print("logging out") # Extract the raw JWT string 
        decoded = jwt.decode( token.credentials, settings.JWT_SECRET, algorithms=[settings.JWT_ALGO] ) 
        print("decoded") 
        await TokenBlacklist.revoke(token.credentials, decoded["exp"])
        print("revoked") 
        return {"status": "success", "message": "Token revoked"} 
    except jwt.JWTError: 
        raise HTTPException(status_code=401, detail="Invalid token")
