"""TOML serializer main class."""
import toml
from userializer import packer
from userializer.serializer import Serializer


class TOMLSerializer(Serializer):

    def dumps(self, obj):
        """Serializes object, class or function to TOML."""
        return toml.dumps(packer.pack(obj))

    def loads(self, string):
        """Deserializes object, class or function from TOML."""
        return packer.unpack(toml.loads(string))
