from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
)

class TransactionBase(BaseModel):
    amount: float
    category: str
    description: str
    is_income: bool
    date: str
    
class TransactionModel(TransactionBase):
    id: int
    
    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
db_dependancy = Annotated(session, Depends(get_db))

models.Base.metadata.create_all(bind=engine)


@app.post('/transactions/', response_model=TransactionModel)
async def create_transactions(transactions: TransactionBase, db: db_dependancy):
    db_transaction = models.Transaction(**transactions.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction