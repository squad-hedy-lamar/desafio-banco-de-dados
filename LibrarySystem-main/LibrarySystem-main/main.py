
from genre import Genre
from author import Author
from book import Book
from copy_class import Copy_class
from library import Library
from user import User

terror = Genre("Terror")
romance = Genre("Romance")

autor1 = Author(id=1, name="Stephen King", phone="12321321", nationality="EUA")
autor2 = Author(id= 2,name="Machado de Asis", phone="2131313", nationality= "Brasil")

livro1 = Book(
  title="Dom Casmurro",
  publisher="Editora do Brasil",
  genres=[romance],
  authors=[autor2],
  max_renewals=3
)

livro2 = Book(
  title="O iluminado",
  publisher="Editora do EUA",
  genres=[terror],
  authors=[autor1],
  max_renewals=1
)

copia1 = Copy_class(code="0001")
copia2 = Copy_class(code="0002")
livro1.add_copy(copia1)
livro1.add_copy(copia2)

copia1 = Copy_class(code="0001")
copia2 = Copy_class(code="0002")
copia3 = Copy_class(code="0003")
livro2.add_copy(copia1)
livro2.add_copy(copia2)
livro2.add_copy(copia3)

biblioteca = Library([livro1, livro2])
# biblioteca.add_book(livro1)
# biblioteca.add_book(livro2)

usuario1 = User(id= 1, name="João", phone="21321321", nationality="Brasileiro")
usuario2 = User(id= 2, name="Maria", phone="21311321", nationality="Brasileiro")

emprestimoJ = biblioteca.borrow_book(livro2, usuario1)
print(f"Empréstimo 1 : {emprestimoJ.copy.code} - {livro2.title} para {emprestimoJ.user.name}")

biblioteca.renew_book(emprestimoJ)

# biblioteca.renew_book(emprestimoJ) número max de renovações atingido

print(f"(Antes de devolver) Livro está emprestado?: {emprestimoJ.copy.borrowed  }")

biblioteca.return_book(emprestimoJ)

print(f"(Antes de devolver) Livro está emprestado?: {emprestimoJ.copy.borrowed}")

emprestimos = biblioteca.list_all_loans()

print("Lista de empréstimos")
for emprestimo in emprestimos:
  print(f"Usuário {emprestimo.user.name} emprestou o livro {emprestimo.book.title} no dia {emprestimo.borrow_date.strftime('%d/%m/%Y')}")

