from datetime import datetime
from sqlalchemy import Integer, String, Text, DateTime, func
from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    sentiment: Mapped[str] = mapped_column(String(20), default="pending") # настроение
    status: Mapped[str] = mapped_column(String(20), default="queued")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

