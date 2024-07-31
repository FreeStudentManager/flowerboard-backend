from sqlmodel import Field, SQLModel


class School(SQLModel, table=True):
    """学校

    Attributes: 
        id: 学校 ID
        name: 校名
        address: 地址
        description: 简介
    """
    id: int | None = Field(default=None, primary_key=True)
    name: str
    address: str
    description: str
