from typing import Union, TypeVar, Generic
from datetime import datetime
from pydantic import BaseModel
from enum import Enum
from random import random

class LoanApplicationState(Enum):
    DRAFT = 1
    WITHDRAWN = 2
    COLLECTING_STAKE = 3
    FULLY_FUNDED = 4
    IN_PROGRESS = 5
    DEFAULT = 6
    COMPLETE = 7

class WalletType(Enum):
    WITHDRAW_ONLY = 1
    DEPOSIT_ONLY = 2
    WITHDRAW_OR_DEPOSIT = 3
    INTERNAL_ONLY = 4

class LoanPaymentState(Enum):
    SCHEDULED = 1
    UPCOMING = 2
    COMPLETED_ON_TIME = 3
    LATE = 4
    COMPLETED_LATE = 5
    MISSED = 6

class WalletStatus(object):

    reasons = {
        101: "missing_user_verification",
        102: "fraud_suspected",
        103: "staked_for_loan"
    }

    def __init__(self, is_frozen, frozen_reason_code):
        self.doc_id: str = random()
        self.is_frozen: bool = is_frozen
        self.frozen_reason_code: int = frozen_reason_code
    
    def to_dict(self):
        return {
            "doc_id": self.doc_id,
            "is_frozen": self.is_frozen,
            "frozen_reason_code": self.frozen_reason_code,
            "frozen_reason_message": self.reasons.get(self.frozen_reason_code)
        }

class LoanApplicationStatus(object):
    def __init__(self, state, next, previous, timestamp):
        self.doc_id: str = random()
        self.state: LoanApplicationState = state
        self.next: Union[LoanApplicationStatus, None] = next
        self.previous: Union[LoanApplicationStatus, None] = previous
        self.timestamp: datetime = timestamp

    def to_dict(self):
        return {
            "doc_id": self.doc_id,
            "state": self.LoanPaymentState,
            "next": self.LoanApplicationStatus,
            "previous": self.LoanApplicationStatus,
            "timestamp": self.timestamp
        }

class LoanPaymentStatus(object):
    def __init__(self, state, next, previous, timestamp):
        self.doc_id: str = random(),
        self.state: LoanPaymentState = state
        self.next: Union[LoanPaymentStatus, None] = next
        self.previous: Union[LoanPaymentStatus, None] = previous
        self.timestamp: datetime = timestamp
        
    def to_dict(self):
        return {
            "doc_id": self.doc_id,
            "state": self.LoanPaymentState,
            "next": self.LoanApplicationStatus,
            "previous": self.LoanApplicationStatus,
            "timestamp": self.timestamp
        }

class Wallet(object):
    def __init__(self, wallet_type, address, key, wallet_status):
        self.doc_id: str = random()
        self.wallet_type: WalletType = wallet_type
        self.address: str = address
        self.key: str = key
        self.status: WalletStatus = wallet_status
        
    def to_dict(self):
        # do not return key in responses
        return {
            "doc_id": self.doc_id,
            "wallet_type": self.wallet_type,
            "address": self.address,
            "status": self.status
        }

class User(object):
    def __init__(self, uid):
        self.uid: str = uid
        
    def to_dict(self):
        return {
            "uid": self.uid
        }

class Loan(object):
    def __init__(
            self,
            principal_in_xno,
            loan_start_date,
            monthly_payment,
            monthly_interest_rate,
            number_of_payment_periods,
            status,
            payment_wallet,
            principal_wallet,
            borrower):
        self.doc_id: str = random()
        self.principal_in_xno: float = principal_in_xno
        self.loan_start_date: datetime = loan_start_date
        self.monthly_payment: float = monthly_payment
        self.monthly_interest_rate: float = monthly_interest_rate
        self.number_of_payment_periods: int = number_of_payment_periods
        self.status: LoanApplicationStatus = status
        self.payment_wallet: Wallet = payment_wallet
        self.principal_wallet: Wallet = principal_wallet
        self.borrower: User = borrower
        
    def to_dict(self):
        return {
            "doc_id": self.doc_id,
            "principal_in_xno": self.principal_in_xno,
            "loan_start_date": self.loan_start_date,
            "monthly_payment": self.monthly_payment,
            "monthly_interest_rate": self.monthly_interest_rate,
            "number_of_payment_periods": self.number_of_payment_periods,
            "status": self.status,
            "payment_wallet": self.payment_wallet,
            "principal_wallet": self.principal_wallet,
            "borrower": self.borrower
        }

class Stake(object):
    def __init__(
            self,
            owner,
            stake_start_date,
            stake_from_wallet,
            yield_wallet,
            monthly_interest_rate,
            monthly_payment,
            number_of_payment_periods):
        self.doc_id: str = random()
        self.owner: User = owner
        self.start_date: datetime = stake_start_date
        self.from_wallet: Wallet = stake_from_wallet
        self.yield_wallet: Wallet = yield_wallet
        self.monthly_interest_rate: float = monthly_interest_rate
        self.monthly_payment: float = monthly_payment
        self.number_of_payment_periods: float = number_of_payment_periods
        
    def to_dict(self):
        return {
            "doc_id": self.doc_id,
            "owner": self.owner,
            "start_date": self.start_date,
            "from_wallet": self.from_wallet,
            "yield_wallet": self.yield_wallet,
            "monthly_interest_rate": self.monthly_interest_rate,
            "monthly_payment": self.monthly_payment,
            "number_of_payment_periods": self.number_of_payment_periods
        }

class LoanPayment(object):
    def __init__(self, loan, due_date, amount_due_in_xno, status):
        self.doc_id: str = random()
        self.loan: Loan = loan
        self.due_date: datetime = due_date
        self.amount_due_in_xno: float = amount_due_in_xno
        self.status: LoanPaymentStatus = status
        
    def to_dict(self):
        return {
            "doc_id": self.doc_id,
            "loan": self.loan,
            "due_date": self.due_date,
            "amount_due_in_xno": self.amount_due_in_xno,
            "status": self.status
        }
