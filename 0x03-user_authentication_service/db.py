#!/usr/bin/env python3
"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User, Base
from sqlalchemy.exc import InvalidRequestError, NoResultFound


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add user to db"""
        s = self._session
        user = User(email=email, hashed_password=hashed_password)
        s.add(user)
        s.commit()
        return user

    def find_user_by(self, **kwargs: str) -> User:
        """find user by either email or hashed psw"""
        s = self._session
        try:
            user = s.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise
        except InvalidRequestError:
            raise
        return user
