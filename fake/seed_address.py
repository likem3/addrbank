from apps.models import Address, Currency


def fake_addresses():
    dict_currency = {
        'doge': 9,
        'usdt': 3,
        'tron': 10,
        'eth': 2,
        'btc': 1
    }

    for name, id in dict_currency.items():
        print(name, id)

        list_address = []
        with open(f'fake/{name}.txt', 'r') as file:
            for line in file:
                list_address.append(
                    Address(
                        address=line.strip(),
                        resource='fake.org',
                        currency=Currency.objects.get(pk=id),
                        created_by_id=1,
                    )
                )
        
        Address.objects.bulk_create(
            list_address
        )

        print(f'{name} saved ...!')