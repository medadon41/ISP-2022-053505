import os
from userializer import json_serializer as json
from tests import mocks


def test_dumps_and_loads():
    ser = json.JSONSerializer()
    s = ser.dumps(mocks.f)
    fun = ser.loads(s)
    assert isinstance(fun(2), float)


def test_dump_and_load():
    ser = json.JSONSerializer()
    file = open("test.json", "w")

    ser.dump(mocks.mul, file.name)
    fun = ser.load(file.name)

    file.close()
    os.remove(os.path.abspath(file.name))

    assert 2 * 2 == fun(2, 2)
