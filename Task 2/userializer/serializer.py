class Serializer:
    """Serializer main (abstract) class."""

    def dumps(self, item: any) -> str:
        pass

    def loads(self, string: str) -> any:
        pass

    def dump(self, item: any, filename: str):
        """Serializes object, class or function and writes them into file."""
        f = open(filename, 'w')
        f.write(self.dumps(item))

    def load(self, filename: str):
        """Reads from file and deserializes object, class or function."""
        f = open(filename, 'r')
        return self.loads(f.read())
