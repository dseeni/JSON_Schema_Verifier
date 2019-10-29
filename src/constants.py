

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
