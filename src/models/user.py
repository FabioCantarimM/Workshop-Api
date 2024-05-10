from pydantic import BaseModel
from typing import Optional

from src.db.connection import Base

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class User(BaseModel):
    id: int   # Role 1
    name: str # Role 1
    area: str # Role 1
    job_description: str # Role 1
    role: int #Role 2 #1 #2 #3
    salary: float # Role 2 
    is_active: bool
    last_evaluation: Optional[str] = None # Role 3 #Positive #Negative #Neutral

class LastEvaluationEnum(Enum):
    excellent = "Excellent"
    good = "Good"
    fair = "Fair"
    poor = "Poor"  

class Db_User(Base):
    __tablename__ =  "users"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    area = Column(String)
    job_description = Column(String)
    role = Column(Integer)
    salary = Column(Float)
    is_active =  Column(Boolean)
    last_evaluation = Column(Enum(LastEvaluationEnum))
    