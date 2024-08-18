from typing import Annotated, Optional
from sqlmodel import SQLModel, Field


class UserCreate(SQLModel):
    name: Annotated[str, Field]
    password: Annotated[str, Field()]
    phone: Annotated[Optional[str], Field()] = None
    email: Annotated[Optional[str], Field()] = None
    account: Annotated[str, Field]
