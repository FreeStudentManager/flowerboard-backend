from fastapi import APIRouter
from sqlmodel import Session, select

from database import engine
from models import Stick, StickComment

router = APIRouter(tags=['Stick'])


@router.get('/', name='Get all sticks')
async def get_all_sticks():
    with Session(engine) as session:
        return session.exec(select(Stick)).all()
