"""
Savor Data :: Data models
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class Project(Base):
    __tablename__ = "project_log"

    id = Column(Integer, primary_key=True)
    time_in = Column(DateTime)
    notes = Column(String)
    location = Column(String)
    engage_log = Column(String)
    time_out = Column(DateTime)


class Engagement(Base):
    __tablename__ = "engage_log"


class Moment(Base):
    __tablename__ = "moment_log"

