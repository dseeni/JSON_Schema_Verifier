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


# notice the multiple inheritence from both SchemaError as a base Exception,
# then from specifically TypeError...
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


# verify type(value) each depth level...
def verify_types(valid, data, path=''):
    # lets assume here that the keys have already been matched OK
    # but do not assume that the keys are necessarily in the same
    # order in both the data and the valid template #

    # decide whether item is dict or not first:
    for key, value in valid.items():
        if isinstance(value, dict):
            # marking the nested dict str as type(dict) via template_type
            template_type = dict
        else:
            # otherwise we can just use the value in the current layer dict
            template_type = value
        data_value = data.get(key, object())
        if isinstance(data_value, template_type):
            continue
        else:
            err_msg = ('incorrect type: ' + path + '.' + key +
                       ' -> expected ' + template_type.__name__ +
                       ', found ' + type(data_value).__name__)
            raise SchemaTypeMismatch(err_msg)

# this goes depth level one at a time, checking keys, then values,
# then identifying the nested dicts in the values of the current depth level,
# the recurcivley moving one level down again
def recurse_validate(valid, data, path=''):
    verify_keys(valid, data, path)
    verify_types(valid, data, path)
    # now we can assume both keys and values on the first layer are verified

    # get good at these if / else inside a comprehension
    dict_type_keys = {key for key, value in valid.items()
                      if isinstance(value, dict)}

    for key in dict_type_keys:
        sub_path = path + '.' + str(key)
        sub_template = valid[key]
        sub_data = data[key]
        recurse_validate(sub_template, sub_data, sub_path)


def validate(valid, data):
    recurse_validate(valid, data, '')


# returns True
# print(verify_schema()(template, john))

# missing 'city' sub dict
# print(verify_schema(template, eric))

# dob:'month':<str> not int!
# print(verify_schema(template, michael))

# extra key error
print(validate(template, rodney))
# print(validate(rodney, template))
