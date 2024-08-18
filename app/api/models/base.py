from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from uuid import uuid4, UUID


class IntPrimaryKey(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    """
    ```python
    id: Optional[int] = None
    ```
    """


class UUIDPrimaryKey(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    """
    ```python
    id: UUID = uuid4()
    ```
    """


class CreateAtColumn(SQLModel):
    """create datetime column"""

    create_at: Optional[datetime] = Field(default_factory=datetime.now, nullable=False)
    """
    ```python
    create_at: Optional[datetime]
    ```
    """


class UpdateAtColumn(SQLModel):
    """update datetime column"""

    update_at: Optional[datetime] = Field(default_factory=datetime.now, nullable=False)
    """
    ```python
    update_at: Optional[datetime]
    ```
    """
