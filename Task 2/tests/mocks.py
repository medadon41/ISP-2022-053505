def mul(a, b):
    return a * b


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


object_person = Person()