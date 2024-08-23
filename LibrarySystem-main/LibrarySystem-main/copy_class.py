class Copy_class:
    def __init__(self, code):
        self.__code = code
        self.__borrowed = False

    @property
    def code(self):
        return self.__code

    @property
    def borrowed(self):
        return self.__borrowed

    @borrowed.setter
    def borrowed(self, value):
        self.__borrowed = value
