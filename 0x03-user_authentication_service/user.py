#!/usr/bin/python3
""" User model"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """class user"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
