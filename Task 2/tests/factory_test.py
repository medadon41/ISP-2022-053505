from userializer.serializer_factory import *
from userializer import json_serializer as json
from userializer import yaml_serializer as yaml
from userializer import toml_serializer as toml


def get_serializer(creator: SerializerCreator()):
    return creator.create_serializer()


def test_json_creator():
    ser = get_serializer(JSONSerializerCreator())
    print(type(ser))
    assert isinstance(ser, json.JSONSerializer)


def test_yaml_creator():
    ser = get_serializer(YAMLSerializerCreator())
    print(type(ser))
    assert isinstance(ser, yaml.YAMLSerializer)


def test_toml_creator():
    ser = get_serializer(TOMLSerializerCreator())
    print(type(ser))
    assert isinstance(ser, toml.TOMLSerializer)
