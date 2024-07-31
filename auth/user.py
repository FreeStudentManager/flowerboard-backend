import secrets
from datetime import datetime, timedelta

import jwt
from fastapi import Depends, HTTPException
from fastapi.security.api_key import APIKeyCookie
from sqlmodel import Session, select

from config import SECRET_KEY
from database import engine
from models.user import UserDB

api_key_schema = APIKeyCookie(name="token", auto_error=False)


def generate_token(user: UserDB, exp: datetime | None = None) -> str:
    if exp is None:
        exp = datetime.now() + timedelta(days=7)

    return jwt.encode(
        {
            'nbf': int(datetime.now().timestamp()),
            'exp': int(exp.timestamp()),
            'sub': user.id,
            'jti': secrets.token_hex(16)
        }, SECRET_KEY
    )


def decode_token(token: str = Depends(api_key_schema)) -> UserDB:
    try:
        decoded = jwt.decode(token)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Expired token")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    session = Session(engine)
    user = session.exec(select(UserDB).where(UserDB.id == decoded['sub'])
                        ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token. Cannot find subject in token."
        )

    return user


__all__ = ['generate_token', 'decode_token']
