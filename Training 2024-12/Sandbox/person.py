
class Person:
    last_id = 0

    def __init__(self, name, residence, id = None):
        if id is None:
            Person.last_id += 1
            self._id = Person.last_id
        else:
            self._id = id
        self._name = name
        self._residence = residence

    def __str__(self):
        return f'Person: {self._name} {self._residence}'

    def __repr__(self):
        return f'Person("{self._name}", "{self._residence}")'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == '':
            raise Exception('Invalid name')
        self._name = name.title()

    def tell(self):
        print(f'Ik ben {self._name} an ik woon in {self._residence}')

    def move(self, new_residence):
        self._residence = new_residence

    @staticmethod
    def clone(person):
        return Person(person._name, person._residence, person._id)

    @classmethod
    def clone(cls, person):
        return cls(person._name, person._residence, person._id)

# ----------------------------------------------------

if __name__ == '__main__':

    p1 = Person('Peter', 'Lhee')
    p2 = Person('Jan', 'Amsterdam', id = 8)
    p3 = Person("Peter", "Lhee")

    print(p1._id)
    print(p2._id)

    print(p1)
    print(str(p1))
    print(repr(p1))

    p1.tell()
    p1.move('Utrecht')
    p1.tell()

    p1.name = 'peer'
    print(p1.name)
    p1.tell()

    p4 = Person.clone(p1)