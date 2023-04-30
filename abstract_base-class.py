from abc import abstractmethod, ABCMeta


class Programming(metaclass=ABCMeta):

    @abstractmethod
    def has_opp(self):
        pass

    def name(self):
        return "Programming"


class Python(Programming):
    def has_opp(self):
        return "true"

    def name(self):
        return "Python"


python = Python()
print(python.has_opp())
print(python.name())
print(Programming.name(python))
