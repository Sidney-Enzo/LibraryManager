class Loan:
    def __init__(self, id: str, book_id: str, user_id: str, loan_date: str, return_date: str=None):
        self.id = id
        self.book_id = book_id
        self.user_id = user_id
        self.loan_date = loan_date
        self.return_date = return_date

    def __repr__(self):
        return f"Loan(ID: {self.id}, Book ID: {self.book_id}, User ID: {self.user_id}, Loan Date: {self.loan_date}, Return Date: {self.return_date})"
