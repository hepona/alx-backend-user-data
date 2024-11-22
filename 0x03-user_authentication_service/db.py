#!/usr/bin/env python3
"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import User, Base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


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
        """add user to database"""
        s = self._session
        user = User(email=email, hashed_password=hashed_password)
        s.add(user)
        s.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """find user by either email or hashed psw"""
        s = self._session
        try:
            user = s.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise
        except InvalidRequestError:
            raise
        return user

    def update_user(self, user_id: int, **kwargs: str) -> None:
        """update user's info"""
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if not hasattr(user, k):
                raise ValueError
            setattr(user, k, v)
        self._session.commit()
