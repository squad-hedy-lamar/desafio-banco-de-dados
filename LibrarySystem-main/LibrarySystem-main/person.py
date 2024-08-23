from abc import ABC

class Person(ABC):
    def __init__(self, id, name, phone, nationality):
        '''
        id: unique identifier of the person
        name: name of person
        phone: phone number of person
        nationality: nationality of person
        '''
        self.__id = id
        self.__name = name
        self.__phone = phone
        self.__nationality = nationality

    @property
    def id(self):
        """Return the unique identifier of the person."""
        return self.__id
    
    @property
    def name(self) :
        """Return the name of the person."""
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def phone(self):
        """Return the phone number of the person."""
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def nationality(self):
        """Return the nationality of the person."""
        return self.__nationality
    
    @nationality.setter
    def nationality(self, value):
        self.__nationality = value
    
    def __str__(self):
        """Return a string about the person."""
        return f"ID: {self.__id}, Name: {self.__name} (Phone: {self.__phone}, Nationality: {self.__nationality})"
    
# Create an instance of the Person class
# person1 = Person(1, "Manu", "19999999999", "Brazil")
# person2 = Person(2, "Emanoela", "199949999", "Brazil")

# print(f"{person1}\n{person2}")


