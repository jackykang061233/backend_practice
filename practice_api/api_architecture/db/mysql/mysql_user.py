import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

load_dotenv()

username = os.getenv('username')
password = os.getenv('password')
db = os.getenv('db')

DATABASE_URL = f'mysql://{username}:{password}@localhost/{db}'
engine = create_engine(DATABASE_URL)

session = Session(bind=engine)

def create_mysql_user(username: str, password: str, database_name: str):
    if not username or not password or not database_name:
        raise ValueError("Username, password, and database_name cannot be empty strings.")
    
    create_user_sql = text(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';")
    grant_privileges_sql = text(f"GRANT CREATE, SELECT, INSERT, DELETE ON `{database_name}`.* TO '{username}'@'localhost';")
    flush_privileges_sql = text("FLUSH PRIVILEGES;")

    # Execute the SQL statements
    session.execute(create_user_sql)
    session.execute(grant_privileges_sql)
    session.execute(flush_privileges_sql)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()