import sqlite3

conexao = sqlite3.connect('biblioteca.db')

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        publisher TEXT NOT NULL,
        genre TEXT NOT NULL,
        copies INTEGER NOT NULL,
        max_renewals INTEGER NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS loan (
        copy_id INTEGER,
        user_id INTEGER,
        borrow_date DATE,
        return_date DATE,
        PRIMARY KEY (copy_id, user_id),
        FOREIGN KEY (copy_id) REFERENCES book(id),
        FOREIGN KEY (user_id) REFERENCES person(id)
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS author (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        nationality TEXT NOT NULL
        
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        nationality TEXT NOT NULL
    )
''')
#inserção de dados person
cursor.execute("INSERT INTO person(name, phone,nationality) VALUES ('Manu','19999999999','Brazil')")
cursor.execute("INSERT INTO person(name, phone,nationality) VALUES ('Emanoela','199949999','Brazil')")
cursor.execute("INSERT INTO person(name, phone,nationality) VALUES ('Priscila','1130899284','Argentina')")
#inserção de dados book
cursor.execute("INSERT INTO book(title, publisher,genre, author, copies, max_renewals) VALUES ('João e Maria','1º edição','Infantojuvenil','Irmãos Grimm',2,2)")
cursor.execute("INSERT INTO book(title, publisher,genre, author, copies, max_renewals) VALUES ('Dom Casmurro', 'Machado de Assis',	'Brasil','Editora do Brasil',2,2)")
cursor.execute("INSERT INTO book(title, publisher,genre, author, copies, max_renewals) VALUES ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry','França','Editora DEF',2,2)")

#inserção de dados author
cursor.execute("INSERT INTO author(name, phone, nationality) VALUES ('Stephen King','123456789','EUA')")
cursor.execute("INSERT INTO author(name, phone, nationality) VALUES ('Machado de Assis','550392302','Brazil')")

#inserção de dados loan
cursor.execute("INSERT INTO loan(  borrow_date, return_date) VALUES ('2022-01-01','2022-01-02')")

#consulta dos dados
'''cursor.execute("SELECT * FROM book")
books = cursor.fetchall()
print("Books:", books)'''

#Loan dados
cursor.execute("""
    SELECT book.title 
    FROM book 
    JOIN loan ON book.id = loan.book_id 
    WHERE loan.return_date > DATE('now')
""")
borrowed_books = cursor.fetchall()
print("Livros emprestados:", borrowed_books)

# Localizar os livros escritos por um autor específico
cursor.execute("""
    SELECT book.title 
    FROM book 
    JOIN author ON book.author_id = author.id 
    WHERE author.name = 'Machado de Assis'
""")
books_by_author = cursor.fetchall()
print("Livros escritos por Machado de Assis:", books_by_author)

# Verificar o número de cópias disponíveis de um determinado livro
cursor.execute("SELECT title, copies FROM book WHERE title = 'Dom Casmurro'")
book_copies = cursor.fetchall()
print("Cópias de 'Dom Casmurro':", book_copies)

# Mostrar os empréstimos em atraso
cursor.execute("""
    SELECT person.name, book.title 
    FROM loan 
    JOIN person ON loan.person_id = person.id 
    JOIN book ON loan.book_id = book.id 
    WHERE loan.return_date < DATE('now')
""")
overdue_loans = cursor.fetchall()
print("Empréstimos em atraso:", overdue_loans)

# Marcar um livro como devolvido (atualizar a data de devolução)
cursor.execute("UPDATE loan SET return_date = '2023-08-01' WHERE id = 1")

# Remover um autor
cursor.execute("DELETE FROM author WHERE name = 'Stephen King'")





conexao.commit()
conexao.close()