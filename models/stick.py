from sqlmodel import Field, SQLModel


class Stick(SQLModel):
    """表白墙上的贴纸

    Attributes: 
        id: 贴纸 ID
        name: 名称
        content: 内容
        creator: 创建者（None 表示匿名）
    """
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=16)
    content: str
    creator: str | None = Field(default=None)


class StickComment(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    stick_id: int | None = Field(default=None, foreign_key="stick.id")
    content: str
    sender: str | None = Field(default=None)
