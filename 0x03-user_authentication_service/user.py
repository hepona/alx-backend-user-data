#!/usr/bin/python3
""" SQLAlchemy model named User for a database table named users"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """SQLAlchemy model named User for a database table named users"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
