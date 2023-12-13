import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, Column, Integer, String, Enum, DateTime, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, validates, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
import re

# load environment variable
load_dotenv()
username = os.getenv('username')
password = os.getenv('password')
db = os.getenv('db')

# 
DATABASE_URL = f'mysql://{username}:{password}@localhost/{db}'
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

association_table = Table(
    'order_item_association',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('order.id')),
    Column('item_id', Integer, ForeignKey('item.id'))
)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    sex = Column(Enum('Male', 'Female', 'Other'))
    created_time = Column(DateTime, default=datetime.now)
    last_login = Column(DateTime, default=datetime.now)

    # Define a relationship with the Order table
    orders = relationship('Order', back_populates='user')

    @validates('email')
    def validate_email(self, key, email):
        # Check if the email format is valid using a simple regular expression
        if not re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email):
            raise ValueError("Invalid email format")
        return email
class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    product_name = Column(String(255), nullable=False)
    quantity = Column(Integer, default=0, nullable=False)
    total_price = Column(Float, default=0.0, nullable=False)
    order_date = Column(DateTime, default=datetime.now)
    order_status = Column(Enum('Accepted', 'Pending', 'Rejected'))
    order_notes = Column(String(100))

    # Define a relationship with the User table
    user = relationship('User', back_populates='orders')
    items = relationship('Item', secondary=association_table, back_populates='orders')

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    price = Column(Float, default=0.0, nullable=False)
    description = Column(String(300))

    orders = relationship('Order', secondary=association_table, back_populates='items')

    created_time = Column(DateTime, default=datetime.now)
    last_update = Column(DateTime)

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



if __name__ == '__main__':
    pass
    # delete_user("joe", "morals")

    # create_user("john@example.com", "joe", "morals", "Male")
    # user = get_user_by_email("john@example.com")
    # print(user.email, user.first_name, user.last_name, user.sex)

    # update_user_email("joe", "morals", "new_email@example.com")
    # user = get_user_by_email("new_email@example.com")
    # print(user.email, user.first_name, user.last_name, user.sex)
