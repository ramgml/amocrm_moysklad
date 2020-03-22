import requests
import json

POST = 'POST'
GET = 'GET'


class HttpException(Exception):
    pass


class HttpClient:
    def __init__(self, url: str):
        self._url = url
        self._session = requests.Session()

    def auth(self, login, api_key):
        auth_data = {
            'USER_LOGIN': login,
            'USER_HASH': api_key
        }
        self._session.post(f'https://{self._url}/private/api/auth.php?type=json', json=auth_data)

    def send(self, method, entity_type, parameters=None, payload=None):
        response = self._session.request(
            method,
            url=self._build_uri(entity_type),
            headers={
                'User-Agent': 'amoCRM-API-client/1.0',
                'Content-Type': 'application/json'
            },
            params=parameters,
            json=payload
        )
        if response.status_code == 200:
            return json.loads(response.text)

        if response.status_code == 204:
            return {}

        raise HttpException(response.text)

    def _build_uri(self, entity_type):
        return f'https://{self._url}/api/v2/{entity_type}'

