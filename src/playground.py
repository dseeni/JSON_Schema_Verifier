class SchemaError(Exception):
    pass


class SchemaKeyMismatch(SchemaError):
    pass


class SchemaTypeMismatch(SchemaError, TypeError):
    pass


def match_keys(data, valid, path):
    # path is just a string containing the current path
    # that we can use to append the extra/missing keys
    # and create a full path for the mismatched keys
    data_keys = data.keys()
    valid_keys = valid.keys()
    # we could just use data_keys ^ valid_keys
    # to get mismatched keys, but I prefer to differentiate
    # between missing and extra keys separately
    extra_keys = data_keys - valid_keys
    missing_keys = valid_keys - data_keys
    # Finally, build up the error state and message
    if missing_keys or extra_keys:
        is_ok = False
        missing_msg = ('missing keys:' +
                       ','.join({path + '.' + str(key)
                                 for key in missing_keys})
                      ) if missing_keys else ''
        extras_msg = ('extra keys:' +
                     ','.join({path + '.' + str(key)
                               for key in extra_keys})
                     ) if extra_keys else ''
        raise SchemaKeyMismatch(' '.join((missing_msg, extras_msg)))


def match_types(data, template, path):
    # assume here that the keys have already been matched OK
    # but do not assume that the keys are necessarily in the same
    # order in both the data and the template
    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict
        else:
            template_type = value
        data_value = data.get(key, object())
        if isinstance(data_value, template_type):
            continue
        else:
            err_msg = ('incorrect type: ' + path + '.' + key +
                       ' -> expected ' + template_type.__name__ +
                       ', found ' + type(data_value).__name__)
            raise SchemaTypeMismatch(err_msg)

def recurse_validate(data, template, path):
    match_keys(data, template, path)
    match_types(data, template, path)

    # Now see if we have nested dictionaries in template
    # (or data, since we know both keys and value data types match)
    dictionary_type_keys = {key for key, value in template.items()
                           if isinstance(value, dict)}
    for key in dictionary_type_keys:
        sub_path = path + '.' + str(key)
        sub_template = template[key]
        sub_data = data[key]
        recurse_validate(sub_data, sub_template, sub_path)



def validate(data, template):
    recurse_validate(data, template, '')
