# key to check against
template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
        },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
            },
        'birthplace': {
            'country': str,
            'city': str
            }
        }
    }

# good key
john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
        },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
            },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
            }
        }
    }

# missing 'city' sub dict
eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
        },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
            },
        'birthplace': {
            'country': 'United Kingdom'
            }
        }
    }

# dob:'month':<str> not int!
michael = {
    'user_id': 102,
    'name': {
        'first': 'Michael',
        'last': 'Palin'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',
            'day': 5
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Sheffield'
        }
    }
}

# extra key error --> 'middle'
rodney = {
    'user_id': 100,
    'name': {
        'first': 'Rodney',
        'middle': 'Lowe',
        'last': 'Cleese'
        },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
            },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
            }
        }
    }
