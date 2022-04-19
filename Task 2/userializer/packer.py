"""Object attributes' packer."""
import builtins
import importlib
import sys
import types
from inspect import getmodule


def pack(obj) -> any:
    """Packs object into a dict."""

    if isinstance(obj, int | str | types.NoneType):
        return obj
    elif isinstance(obj, tuple):
        return {"tuple": pack_elems(obj)}
    elif isinstance(obj, list):
        return {"list": pack_elems(obj)}
    elif isinstance(obj, dict):
        return {"dict": obj}
    elif isinstance(obj, bytes):
        return {"bytes": obj.hex()}
    elif isinstance(obj, types.MappingProxyType):
        item_dict = dict(obj)
        for key in item_dict.keys():
            item_dict[key] = pack(item_dict[key])
        return item_dict

    elif isinstance(obj, types.CodeType):
        return {"code": pack_attrs(obj)}
    elif isinstance(obj, types.FunctionType):
        return {"func": pack(obj.__code__)}
    elif isinstance(obj, type):
        attribs_dict = dict(obj.__dict__)
        for key in attribs_dict.keys():
            attribs_dict[key] = pack(attribs_dict[key])
        attribs_dict['__annotations__'] = None
        return {"type": {"name": obj.__name__, "attribs": attribs_dict}}

    if (getmodule(type(obj)).__name__ in sys.builtin_module_names):
        return None

    else:
        obj_dict = pack(obj.__dict__)
        obj_type = pack(type(obj))
        return {"object": {"obj_type": obj_type, "obj_dict": obj_dict}}


def pack_elems(obj) -> dict[str, any]:
    """Packs elements of iterable types."""
    elements = dict()
    for i in range(len(obj)):
        elements[f"el{i}"] = pack(obj[i])
    return elements


def pack_attrs(obj) -> dict[str, any]:
    """Packs attributes of the object."""
    elements = dict()
    pub_attributes = list(
        filter(lambda item: not item.startswith('_'), dir(obj)))
    for attr in pub_attributes:
        elements[attr] = pack(obj.__getattribute__(attr))
    return elements


def unpack(obj: dict[str, any]):
    """Unpacks dict into object."""
    if not isinstance(obj, dict):
        return obj

    for (key, value) in obj.items():
        if(key == 'tuple'):
            if value is None:
                return ()
            return tuple([unpack(element) for element in value.values()])
        elif(key == 'list'):
            return [unpack(element) for element in value.values()]
        elif(key == 'dict'):
            return value
        elif(key == 'bytes'):
            return bytes.fromhex(value)
        elif(isinstance(value, int | float | str)):
            return value
        elif(key == 'type'):
            import __main__
            globals().update(__main__.__dict__)

            obj_type = getattr(__main__, value['name'], None)
            serialized = pack(obj_type)

            attribs = value['attribs']
            for key in attribs.keys():
                attribs[key] = unpack(attribs[key])

            obj_type = type(
                value['name'],
                (object, ),
                attribs
            )

            return obj_type

        elif(key == 'func'):
            import __main__
            globals().update(__main__.__dict__)
            def func(): pass
            func.__code__ = unpack(value)
            for name in func.__code__.co_names:
                if builtins.__dict__.get(name, 42) == 42:
                    try:
                        builtins.__dict__[name] = importlib.import_module(name)
                    except ModuleNotFoundError:
                        builtins.__dict__[name] = 42
            return func

        elif(key == 'code'):
            return types.CodeType(
                unpack(value["co_argcount"]),
                unpack(value["co_posonlyargcount"]),
                unpack(value["co_kwonlyargcount"]),
                unpack(value["co_nlocals"]),
                unpack(value["co_stacksize"]),
                unpack(value["co_flags"]),
                unpack(value["co_code"]),
                unpack(value["co_consts"]),
                unpack(value["co_names"]),
                unpack(value["co_varnames"]),
                "deserialized",
                unpack(value["co_name"]),
                unpack(value["co_firstlineno"]),
                unpack(value["co_lnotab"]),
                unpack(value["co_freevars"]),
                unpack(value["co_cellvars"])
            )

        elif(key == 'object'):
            obj_type = unpack(value['obj_type'])
            obj_dict = unpack(value['obj_dict'])

            try:
                obj = object.__new__(obj_type)
                obj.__dict__ = obj_dict
                for (key, value) in obj_dict.items():
                    setattr(obj, key, value)
            except TypeError:
                obj = None
            return obj
