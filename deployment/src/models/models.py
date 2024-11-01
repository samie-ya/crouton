from sqlalchemy import Column, ForeignKey, String, Boolean, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, unique=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    email_validated = Column(Boolean, default=False)
    active = Column(Boolean, default=True)
    temporary_password = Column(Boolean, default=False)
    date_registered = Column(DateTime, default=datetime.utcnow)
    last_modified = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, unique=True)
    barcode = Column(String, unique=True)
    available = Column(Boolean, default=False)
    total_available = Column(Integer)
