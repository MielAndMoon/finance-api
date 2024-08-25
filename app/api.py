from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app import service
from app.database import get_db
from .schemas import TransactionModel


router = APIRouter()


@router.post('/transactions', response_model=TransactionModel)
async def create_transaction(transaction: TransactionModel, db: Session = Depends(get_db)):
    return service.insert_transaction(db, transaction)


@router.get('/transactions', response_model=list[TransactionModel])
async def read_transactions(db: Session = Depends(get_db), skip: int = 0, limit: int = 100,):
    transactions = service.get_transactions(db, skip=skip, limit=limit)
    return transactions
