# models are going to be the table for sqlite3 application


from database import Base
from sqlalchemy import String, Column, Boolean, Float, Integer

class Transaction(Base):
    __tablename = 'tansaction'
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    is_income = Column(Boolean)
    date = Column(String)