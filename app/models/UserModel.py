from sqlalchemy import Column, Integer, String
from app.configs.postgres_database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    company = Column(String, nullable=True)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
