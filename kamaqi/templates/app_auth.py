APP_AUTH=\
"""
#Python
import uuid
from jose import jwt
from pydantic.networks import EmailStr
from passlib.context import CryptContext
from datetime import datetime, timedelta

#FastAPI
from fastapi.security import OAuth2PasswordBearer

#App
from {{app}}.settings import TokensConfig

#Database
from database import models
from sqlalchemy.orm import Session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password:str):
    return pwd_context.hash(password)

def create_user_token(data: dict,tokens_config:TokensConfig):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=tokens_config.TIME_DELTA)
    scope = "access_token"
    to_encode.update({"exp": expire})
    to_encode.update({"scope": scope})

    encoded_jwt=jwt.encode(to_encode,
                           tokens_config.SECRET_KEY,
                           algorithm=tokens_config.JMV_ALGORITHM)
    return encoded_jwt
"""