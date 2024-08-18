from sqlmodel import Field
from app.api.config.database_table import TableName
from app.api.models.base import IntPrimaryKey, CreateAtColumn, UpdateAtColumn


class User(IntPrimaryKey, CreateAtColumn, UpdateAtColumn, table=True):
    __tablename__ = TableName.User

    name: str = Field(index=True, nullable=False)
    password: str = Field(nullable=True)
    phone: str = Field(nullable=True, unique=True)
    email: str = Field(nullable=True, unique=True)
    account: str = Field(index=True, nullable=False, unique=True)
