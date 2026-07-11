from DateTime import DateTime, Timezones
from sqlalchemy import String, Float, Integer, Datetime, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base 


class Position(Base):
    __tablename__ = "discinformation"

    id.Mapped[int] = mapped_column(Integer, primary_key=True)
    filesystem: Mapped[str] = mapped_column(String(40), index = True)
    size: Mapped[str] = mapped_column(String(10), index = True)
    used: Mapped[str] = mapped_column(String(10), index = True)
    available: Mapped[str] = mapped_column(String(10), index = True)
    capacity: Mapped[str] = mapped_column(String(10), index = True)
    mounted_on: Mapped[str] = mapped_column(String(10), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    