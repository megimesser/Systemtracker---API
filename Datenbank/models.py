from datetime import datetime, timezone
from sqlalchemy import String, Float, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship #TIMESTAMP
from Datenbank.db import Base 


class Datentraeger(Base):
    __tablename__ = "discinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    host: Mapped[str] = mapped_column(String(300), index = True)
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
    host: Mapped[str] = mapped_column(String(300), index = True)
    marker: Mapped[str] = mapped_column(String(300), index = True)
    total: Mapped[str] = mapped_column(String(300), index = True)
    used: Mapped[str] = mapped_column(String(300), index = True)
    free: Mapped[str] = mapped_column(String(300), index = True)
    available: Mapped[str] = mapped_column(String(300), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    # oder
    #erfasst_am = Column(TIMESTAMP(timezone=true), nullable = False, server_deafult=text("now()"))


class Sysinfo(Base):
    __tablename__ = "sysinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    host: Mapped[str] = mapped_column(String(300), index = True)
    uptime: Mapped[str] = mapped_column(String(300), index = True)
    users: Mapped[str] = mapped_column(String(300), index = True)
    load_averages: Mapped[str] = mapped_column(String(300), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class Docker(Base):
    __tablename__ = "dockerinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    host: Mapped[str] = mapped_column(String(300), index = True)
    image: Mapped[str] = mapped_column(String(300), index = True)
    name: Mapped[str] = mapped_column(String(300), index = True)
    ports: Mapped[str] = mapped_column(String(300), index = True)
    runtime: Mapped[str] = mapped_column(String(300), index = True)
    status: Mapped[str] = mapped_column(String(300), index = True)

    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class Temp(Base):
    __tablename__ = "temperaturinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    host: Mapped[str] = mapped_column(String(300), index = True)
    temp: Mapped[str] = mapped_column(String(300), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class Proc(Base):
    __tablename__ = "prozessinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    host: Mapped[str] = mapped_column(String(300), index = True)
    user: Mapped[str] = mapped_column(String(300), index = True)
    pid: Mapped[str] = mapped_column(String(300), index = True)
    Mem: Mapped[str] = mapped_column(String(300), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )


class Cpu(Base):
    __tablename__ = "cpuinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    host: Mapped[str] = mapped_column(String(300), index = True)
    user: Mapped[str] = mapped_column(String(300), index = True)
    pid: Mapped[str] = mapped_column(String(300), index = True)
    CPU: Mapped[str] = mapped_column(String(300), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

class Host(Base):
    __tablename__="hostinformation"

    id:Mapped[int] = mapped_column(Integer, primary_key = True)
    host: Mapped[str] = mapped_column(String(300), index = True)
    system: Mapped[str] = mapped_column(String(300), index = True)
    hostname: Mapped[str] = mapped_column(String(300), index = True)
    kernel: Mapped[str] = mapped_column(String(300), index = True)
    architecture: Mapped[str] = mapped_column(String(300), index = True)
    erfasst_am: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )






