"""Factory which creates serializers."""
from userializer import serializer
from userializer import json_serializer
from userializer import yaml_serializer
from userializer import toml_serializer


class SerializerCreator:
    """Creator class which declares factory method."""

    def create_serializer(self) -> serializer.Serializer:
        """Creates serializer."""
        pass


class JSONSerializerCreator(SerializerCreator):
    """Creator which creates JSON serializer."""

    def create_serializer(self) -> serializer.Serializer:
        """Creates JSON serializer."""
        return json_serializer.JSONSerializer()


class YAMLSerializerCreator(SerializerCreator):
    """Creator which creates YAML serializer."""

    def create_serializer(self) -> serializer.Serializer:
        """Creates YAML serializer."""
        return yaml_serializer.YAMLSerializer()


class TOMLSerializerCreator(SerializerCreator):
    """Creator which creates TOML serializer."""

    def create_serializer(self) -> serializer.Serializer:
        """Creates TOML serializer."""
        return toml_serializer.TOMLSerializer()