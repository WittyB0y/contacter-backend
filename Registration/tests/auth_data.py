import random

URL = 'http://127.0.0.1:8000/api/v1/'
URLS = {
    'register': f'{URL}register/',
}
DATA = {
    'username': f'test_user_{random.randint(10000, 999999)}_test_user',
    'password': f'@#{random.randint(10000, 100000)}jdshfjhj',
    'email': f'test_e_m_a_i_l_{random.randint(11000, 100000)}@site{random.randint(1000, 100000)}.com',
}
