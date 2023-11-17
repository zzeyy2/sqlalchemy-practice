from sqlalchemy import Column
from sqlalchemy.sql import sqltypes as types
from datetime import datetime
from database.models import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(types.Integer, primary_key=True)
    user_id = Column(types.Integer, nullable=False, unique=True)
    username = Column(types.String)
    full_name = Column(types.String)
    joined = Column(types.Integer, default=int(datetime.now().timestamp()))