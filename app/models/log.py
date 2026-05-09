from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class Log(Base):

    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)

    agent = Column(String)

    event = Column(String)

    latency = Column(Float)