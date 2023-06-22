import requests as r

from auth_data import URLS, DATA


def test_regiser_user():
    result = r.post(URLS['register'], data=DATA)
    assert type(result.json()) == dict, f'Wrong type, Excepted dict, but gotten\n {type(result.json())}'
    assert len(result.json()) == 3, f'Excepted result dict(id, email, username), but gotten\n{result.json()}'
    assert result.status_code == 201, f'Excepted 200, but returned {result.status_code}.'
