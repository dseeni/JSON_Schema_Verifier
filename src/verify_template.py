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


def verify_dict(schema_key, sample):
    template_keys = schema_key.keys()
    sample_keys = sample.keys()

    # at each depth level, check against extra keys
    if len(template_keys - sample_keys) > 0:
        raise KeyError('Missing Keys:', template_keys - sample_keys)
    if len(sample_keys - template_keys) > 0:
        raise KeyError('Extra Keys:', sample_keys - template_keys)
    # if we have non dictionary keys present...(we're in the deepest branches)
    # traverse the deeper branches recursively checking against schema_key
    for key in template_keys:
        if isinstance(schema_key[key], dict):
            verify_dict(schema_key[key], sample[key])
        else:
            try:
                assert isinstance(sample[key], schema_key[key])
            except AssertionError:
                raise TypeError('value:', sample.get(key),
                                'of type', type(sample.get(key)),
                                'does not match schema type',
                                schema_key.get(key))
    return True


# returns True
# print(verify_dict(template, john))

# missing 'city' sub dict
# print(verify_dict(template, eric))

# dob:'month':<str> not int!
print(verify_dict(template, michael))

# extra key error
# print(verify_dict(template, rodney))
