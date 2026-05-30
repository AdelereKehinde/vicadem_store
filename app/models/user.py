from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from datetime import datetime

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    fullname = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    hashed_password = Column(
        String,
        nullable=True
    )

    google_id = Column(
        String,
        nullable=True
    )

    avatar = Column(
        String,
        nullable=True
    )

    role = Column(
        String,
        default="user"
    )

    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )