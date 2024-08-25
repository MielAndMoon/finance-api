from app.models import Transaction
from sqlalchemy.orm import Session

from app.schemas import TransactionModel


def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Transaction).offset(skip).limit(limit).all()


def insert_transaction(db: Session, transaction: TransactionModel):
    db_transaction = Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
