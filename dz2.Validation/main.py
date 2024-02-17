from typing import List
from pydantic import BaseModel


class User(BaseModel):
    name: List[str]
    mail: str
    address: str


class Bank(BaseModel):
    name: str
    rating: int
    opened: str


class Cards(BaseModel):
    cartholder: User
    which_bank: Bank
    opened: str


class Balance(BaseModel):
    card: Cards
    amount: float
    currency: str


user_1 = User(name='one', mail='test@test.com', address='imeetsya')
bank_1 = Bank(name='Obman', rating=1, opened='ochdavno')
card_1 = Cards(cartholder=user_1, which_bank=bank_1, opened='davno')
balance_1 = Balance(card=card_1, amount=100.1, currency='ZBS')

print(balance_1.amount)