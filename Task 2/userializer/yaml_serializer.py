"""YAML serializer main class."""
import yaml
from userializer import packer
from userializer.serializer import Serializer


class YAMLSerializer(Serializer):

    def dumps(self, obj):
        """Serializes object, class or function to YAML."""
        return yaml.dump(packer.pack(obj))

    def loads(self, string):
        """Deserializes object, class or function from YAML."""
        return packer.unpack(yaml.safe_load(string))
