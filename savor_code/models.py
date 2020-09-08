"""
Savor Data :: Data models
"""

from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql


Base = declarative_base()


class Project(Base):
    __tablename__ = "project_log"

    id = Column(Integer, primary_key=True)
    airtable_id = Column(String)
    time_in = Column(DateTime)
    notes = Column(Text)
    location = Column(String)
    engage_log = Column(postgresql.ARRAY(String))
    time_out = Column(DateTime)
    duration = Column(Integer)
    created = Column(DateTime)
    modified = Column(DateTime)


class Engagement(Base):
    __tablename__ = "engage_log"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    time_in = Column(DateTime)
    mental = Column(postgresql.ARRAY(String))
    physical = Column(postgresql.ARRAY(String))
    tags = Column(postgresql.ARRAY(String))
    subloc = Column(postgresql.ARRAY(String))
    mental_note = Column(Text)
    physical_note = Column(Text)
    moment_log = Column(postgresql.ARRAY(String))
    who = Column(postgresql.ARRAY(String))
    dose = Column(postgresql.ARRAY(String))
    project_location = Column(String)
    location = Column(String)
    money = Column(postgresql.ARRAY(String))
    todo = Column(postgresql.ARRAY(String))
    idea = Column(postgresql.ARRAY(String))
    time_out = Column(DateTime)
    duration = Column(Integer)
    created = Column(DateTime)
    modified = Column(DateTime)
    project_log = Column(String)
    id_num = Column(Integer)
    wishlist = Column(postgresql.ARRAY(String))


class Moment(Base):
    __tablename__ = "moment_log"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    time_in = Column(DateTime)
    time_out = Column(DateTime)
    duration = Column(Integer)
    title = Column(String)
    physical = Column(postgresql.ARRAY(String))
    physical_note = Column(Text)
    dose = Column(postgresql.ARRAY(String))
    mental = Column(postgresql.ARRAY(String))
    subloc = Column(postgresql.ARRAY(String))
    mental_note = Column(Text)
    tags = Column(postgresql.ARRAY(String))
    todo = Column(postgresql.ARRAY(String))
    money = Column(postgresql.ARRAY(String))
    who = Column(postgresql.ARRAY(String))
    idea = Column(postgresql.ARRAY(String))
    created = Column(DateTime)
    modified = Column(DateTime)
    project_log = Column(String)
    id_num = Column(Integer)
    wishlist = Column(postgresql.ARRAY(String))
