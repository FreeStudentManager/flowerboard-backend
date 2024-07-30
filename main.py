from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel

from database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(
    title='FlowerBoard Backend API',
    version='0.0.1-alpha.1',
    license_info={
        'name': 'GPL-3.0',
        'url': 'https://www.gnu.org/licenses/gpl-3.0.en.html#license-text'
    },
    lifespan=lifespan
)


@app.get(
    "/ping",
    name="ping",
    summary="Ping",
    description="Ping",
    response_model=str,
    tags=['Utils'],
    responses={
        200:
            {
                "description": "返回一个字符串，内容为 pong",
                'content': {
                    'application/json': {
                        'example': 'pong'
                    }
                }
            }
    }
)
def ping():
    return 'pong'
