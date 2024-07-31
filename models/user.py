from sqlmodel import Field, SQLModel


class UserDB(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    username: str = Field(description='用户名')
    password_digest: str = Field(description='密码摘要')
    email: str | None = Field(default=None, description='邮箱')
    avatar: str | None = Field(default=None, description='头像')


class UserIn(SQLModel):
    username: str = Field(description='用户名')
    password: str = Field(description='密码')
    email: str | None = Field(default=None, description='邮箱')
    avatar: str | None = Field(default=None, description='头像')


class UserOut(SQLModel):
    id: str | None = Field(default=None)
    username: str = Field(description='用户名')
    email: str | None = Field(default=None, description='邮箱')
    avatar: str | None = Field(default=None, description='头像')
