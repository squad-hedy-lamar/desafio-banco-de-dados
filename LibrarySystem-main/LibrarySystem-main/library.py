from datetime import datetime
from loan import Loan
class Library():

    def __init__(self,books):
        self.__books = books
        self.__loans = []

    def __str__(self):
        return f'Books: {self.__books}\nLoans: {self.__loans}'

    @property
    def books(self):
        return self.__books
    
    def books(self,booksList):
        # check if the parameter's value is from list type
        if isinstance(booksList,list):
            self.__books = booksList
        else:
            raise
        ValueError('Invalid type! The parameter must be of type list.')

    
    @property
    def loans(self):
        return self.__loans

    def loans(self,loansList:list):
        # check if the parameter's value is from list type
        if isinstance(loansList,list):
            self.__loans = loansList
        else:
            raise ValueError('Invalid type! The parameter must be of type list.')


    def add_book(self, book):
        self.__books.append(book)

    def borrow_book(self, book, user):
        copy = book.borrow_copy()
        if copy :
            loan = Loan(copy, user, datetime.now(), None, book)
            self.__loans.append(loan)
            return loan
        return None
    
    def return_book(self, loan):
        loan.return_date = datetime.now()
        loan.copy.borrowed = False

    def renew_book(self, loan):
        loan.renew_book()

    def list_all_loans(self):
        return self.__loans



# library = Library(['teste1','teste2'],['teste3','teste4'])
# print(library)

       
    
