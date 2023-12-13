# implementation/user_service.py

from typing import List, Optional
from sqlalchemy.orm import Session
from schemas import User

class UserService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def create_user(self, email: str, first_name: str, last_name: str, sex: str) -> None:
        user = User(email=email, first_name=first_name, last_name=last_name, sex=sex)
        session = self.db
        session.add(user)
        session.commit()
        session.close()
    def get_user_by_email(self, email: str) -> Optional[User]:
        session = self.db
        user = session.query(User).filter(User.email == email).first()
        session.close()
        return user

    def update_user_email(self, first_name: str, last_name: str, new_email: str) -> None:
        session = self.db
        user = session.query(User).filter(User.first_name == first_name).filter(User.last_name == last_name).first()
        if user:
            user.email = new_email
            session.commit()
        session.close()

    def delete_user(self, first_name: str, last_name: str) -> None:
        session = self.db
        user = session.query(User).filter(User.first_name == first_name).filter(User.last_name == last_name).first()
        if user:
            session.delete(user)
            session.commit()
        session.close()

