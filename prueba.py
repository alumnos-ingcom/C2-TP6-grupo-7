
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return Couple(self, other)


class Couple:
    def __init__(self, Person1: Person, Person2: Person):
        self.p1 = Person1
        self.p2 = Person2
        self.names = f'We are {p1.name} and {p2.name}.'
    # behavior when print(object)
    def __repr__(self) -> str:
        return f'We are {p1.name} and {p2.name}.'
    def __call__(self, *args: any, **kwds: any) -> any:
        print('A new couple was created!')
    def __len__(self):
        return 2


p1 = Person('Male', 25)
p2 = Person('Female', 25)
c = p1 + p2
c() # execute __call__ class method
print(c)
print(len(c))