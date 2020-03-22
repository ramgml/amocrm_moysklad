from amocrm.api import build_filters


def test_build_filters():
    filters = {
        'date_create': {
            'from': 1539026320,
            'to': 1539026399
        },
        'active': 1
    }

    result = {
        'filter[date_create][from]': 1539026320,
        'filter[date_create][to]': 1539026399,
        'filter[active]': 1
    }

    assert result == build_filters(filters, 'filter')
