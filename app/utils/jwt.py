from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY

ALGORITHM = "HS256"
EXPIRE_MINUTES = 60 * 24  # 1 day

def create_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None