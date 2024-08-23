from book import Book

class Loan:
    def __init__(self, copy, user, borrow_date, return_date, book):
        self.copy = copy
        self.user = user
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.renewals = 0
        self.book = book

    @property
    def status(self):
        if self.return_date is None:
            return "Borrowed"
        return "Returned"
    
    def renew_book(self):
        if self.renewals < self.book.max_renewals:
            self.renewals += 1
        else:
            raise ValueError("O número máximo de renovações foi atingido para esse livro.")
