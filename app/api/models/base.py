from sqlmodel import SQLModel, Field, BigInteger, Column
from datetime import datetime
from typing import Optional
from uuid import uuid4, UUID


class IntPrimaryKey(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)


class BigIntPrimaryKey(SQLModel):
    id: Optional[int] = Field(
        default=None, primary_key=True, sa_column=Column(BigInteger())
    )


class UUIDPrimaryKey(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True)


class CreateAtColumn(SQLModel):
    """create datetime column"""

    create_at: Optional[datetime] = Field(default_factory=datetime.now, nullable=False)


class UpdateAtColumn(SQLModel):
    """update datetime column"""

    update_at: Optional[datetime] = Field(default_factory=datetime.now, nullable=False)
