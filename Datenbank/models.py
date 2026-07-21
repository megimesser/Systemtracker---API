from datetime import datetime, timezone
from sqlalchemy import String, Float, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from Datenbank.db import Base 


class Datentraeger(Base):
    __tablename__ = "discinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    filesystem: Mapped[str] = mapped_column(String(300), index = True)
    size: Mapped[str] = mapped_column(String(300), index = True)
    used: Mapped[str] = mapped_column(String(300), index = True)
    available: Mapped[str] = mapped_column(String(300), index = True)
    capacity: Mapped[str] = mapped_column(String(300), index = True)
    mounted_on: Mapped[str] = mapped_column(String(300), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class Ram(Base):
    __tablename__ = "raminformation"

    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    marker: Mapped[str] = mapped_column(String(300), index = True)
    total: Mapped[str] = mapped_column(String(300), index = True)
    used: Mapped[str] = mapped_column(String(300), index = True)
    free: Mapped[str] = mapped_column(String(300), index = True)
    available: Mapped[str] = mapped_column(String(300), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class Sysinfo(Base):
    __tablename__ = "sysinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    uptime: Mapped[str] = mapped_column(String(300), index = True)
    users: Mapped[str] = mapped_column(String(300), index = True)
    load_averages: Mapped[str] = mapped_column(String(300), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class Docker(Base):
    __tablename__ = "Dockerinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    image: Mapped[str] = mapped_column(String(300), index = True)
    runtime: Mapped[str] = mapped_column(String(300), index = True)
    status: Mapped[str] = mapped_column(String(300), index = True)

    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class Temp(Base):
    __tablename__ = "Temperaturinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    temp: Mapped[str] = mapped_column(String(300), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class Proc(Base):
    __tablename__ = "Prozessinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    user: Mapped[str] = mapped_column(String(300), index = True)
    pid: Mapped[str] = mapped_column(String(300), index = True)
    Mem: Mapped[str] = mapped_column(String(300), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class Cpu(Base):
    __tablename__ = "Cpuinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    user: Mapped[str] = mapped_column(String(300), index = True)
    pid: Mapped[str] = mapped_column(String(300), index = True)
    CPU: Mapped[str] = mapped_column(String(300), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )





