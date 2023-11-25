from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )


class PlugStatus(Base, TimestampMixin):
    __tablename__ = 'plug_status'

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String)
    device_type = Column(String)
    hub_device_id = Column(String)
    power = Column(String)
    voltage = Column(Float)
    weight = Column(Float)
    electricity_of_day = Column(Integer)
    electric_current = Column(Float)
    version = Column(String)
