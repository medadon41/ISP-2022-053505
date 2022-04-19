import os
from userializer import toml_serializer as toml
from tests import mocks


def test_dumps_and_loads():
    ser = toml.TOMLSerializer()
    s = ser.dumps(mocks.mul)
    fun = ser.loads(s)
    assert 2 * 2 == fun(2, 2)


def test_dump_and_load():
    ser = toml.TOMLSerializer()
    file = open("test.json", "w")

    ser.dump(mocks.mul, file.name)
    fun = ser.load(file.name)

    file.close()
    os.remove(os.path.abspath(file.name))

    assert 2 * 2 == fun(2, 2)
