from sqlalchemy import Integer, String, Column

from database import Database

class Users(Database):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    description = Column(String, index=True)