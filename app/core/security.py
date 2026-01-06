from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ----------------------------
# Password hashing
# ----------------------------
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# ----------------------------
# JWT token generation
# ----------------------------
def create_access_token(payload: dict, expires_minutes: int | None = None) -> str:
    data = payload.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    data["exp"] = expire
    return jwt.encode(data, settings.JWT_SECRET, algorithm=settings.JWT_ALGO)