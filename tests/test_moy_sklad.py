from moy_sklad.serializers import to_camelcase


def test_to_camelcase():
    name1 = 'account_id'
    name2 = 'payment_item_type'

    assert 'accountId' == to_camelcase(name1)
    assert 'paymentItemType' == to_camelcase(name2)
