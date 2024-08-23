from person import Person
class User(Person):
    def __init__(self, id, name, phone, nationality):
        # Chamando o construtor da classe mãe (Person)
        super().__init__(id, name, phone, nationality)
