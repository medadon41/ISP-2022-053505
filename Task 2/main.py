from userializer.serializer_factory import *
from cmd import swap


class Person:
    """Example class."""

    def __init__(self, name='test', age=32) -> None:
        """Initialize."""
        self.name = name
        self.age = age

    name: str
    age: int

    def get_age(self):
        """Return age of person."""
        return self.age

    def greet(self):
        """Say hello."""
        print('Hello')


def some_thing(creator: SerializerCreator()):
    """Serialize and deserialize example object."""
    serializer1 = creator.create_serializer()
    print(type(serializer1))
    person = Person
    s = serializer1.dumps(person)
    res = serializer1.loads(s)

# some_thing(JsonSerializerCreator())
# some_thing(JsonSerializerCreator())


if __name__ == "__main__":
    swap.convert()