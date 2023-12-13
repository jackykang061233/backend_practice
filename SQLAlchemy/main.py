from sqlalchemy import create_engine, Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates, sessionmaker
import re

# DATABASE_URL = 'mysql://visitor:88888888@localhost/demo'
DATABASE_URL = 'mysql://root:YnW=9g66UJQmQj3y@localhost/demo'
engine = create_engine(DATABASE_URL, echo=True)  # Set echo=True for debugging

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    email = Column(String(255), unique=True, nullable=True)

    @validates('email')
    def validate_email(self, key, email):
        # Check if the email format is valid using a simple regular expression
        if not re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email):
            raise ValueError("Invalid email format")
        return email
    

# Create the table
Base.metadata.create_all(engine)

# # Create a session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_user(name: str, email: str):
    user = User(name=name, email=email)
    session = SessionLocal()
    session.add(user)
    session.commit()
    session.close()
def get_user_by_name(name: str):
    session = SessionLocal()
    user = session.query(User).filter(User.name == name).first()
    session.close()
    return user

def update_user_email(name: str, new_email: str):
    session = SessionLocal()
    user = session.query(User).filter(User.name == name).first()
    if user:
        user.email = new_email
        session.commit()
    session.close()

def delete_user(name: str):
    session = SessionLocal()
    user = session.query(User).filter(User.name == name).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()

delete_user("john_doe")

create_user("john_doe", "john@example.com")
user = get_user_by_name("john_doe")
print(user.name, user.email)

update_user_email("john_doe", "new_email@example.com")
user = get_user_by_name("john_doe")
print(user.name, user.email)

