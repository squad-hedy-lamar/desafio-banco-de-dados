#import da outra classe que será implementada
from person import Person

class Author(Person):
    def __init__(self,id, name, phone, nationality):
        super().__init__(id,name, phone, nationality)