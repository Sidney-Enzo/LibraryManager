from models.loan import Loan
from database.db_manager import db_manage

class LoanManager:
    def __init__(self):
        self.db = db_manage

    