# # ----------------------------------------------------------------------------
# Project 1
# In this project our goal is to validate one dictionary structure against a
# template dictionary.
#
# A typical example of this might be working with JSON data inputs in an API.
# You are trying to validate this received JSON against some kind of template
# to make sure the received JSON conforms to that template (i.e. all the keys
# and structure are identical - value types being important, but not the value
# itself - so just the structure, and the data type of the values).
#
# To keep things simple we'll assume that values can be either single values
# (like an integer, string, etc), or a dictionary, itself only containing single
# values or other dictionaries, recursively. In other words, we're not going to
# deal with lists as possible values. Also, to keep things simple, we'll assume
# that all keys are required, and that no extra keys are permitted.
#
# In practice we would not have these simplifying assumptions, and although we
# could definitely write this ourselves, there are many 3rd party libraries that
# already exist to do this
# (such as json schema, marshmallow, and many more, some
# of which I'll cover lightly in some later videos.)
# # ----------------------------------------------------------------------------
from src.constants import *


class SchemaError(Exception):
    pass


class SchemaKeyMismatch(SchemaError):
    pass


class SchemaTypeMismatch(SchemaError, TypeError):
    pass


def verify_keys(valid, data, path=''):
    valid_keys = valid.keys()
    data_keys = data.keys()
    missing = valid_keys - data_keys
    extra = data_keys - valid_keys
    if extra or missing:
        missing_msg = (('missing keys:' + ','.join({path + '.' + str(key)
                                                  for key in missing}))
                       if missing else '')
        extra_msg = (('extra keys:' + ','.join({path + '.' + str(key)
                                                for key in extra})
                      if extra else ''))
        raise SchemaKeyMismatch(' '.join((missing_msg, extra_msg)))


def verify_types(valid, data, path=''):
    # first figure out if the value to be verified is another dict or not
    for key, value in data.items():
        if isinstance(value, dict):
            template_type = dict
        else:
            template_type = value


def verify_schema(valid, data, path=''):
    verify_keys(valid, data, path)


    # if we have non dictionary keys present...(we're in the deepest branches)
    # traverse the deeper branches recursively checking against schema_key
    for key in template_keys:
        if isinstance(valid[key], dict):
            verify_schema(valid[key], data[key])
        else:
            try:
                assert isinstance(data[key], valid[key])
            except AssertionError as a:
                print(data.get(key), type(data.get(key)),
                      'does not match', valid.get(key))
                raise a
    return True


# returns True
# print(verify_schema()(template, john))

# missing 'city' sub dict
# print(verify_schema(template, eric))

# dob:'month':<str> not int!
# print(verify_schema(template, michael))

# extra key error
print(verify_keys(template, rodney))
