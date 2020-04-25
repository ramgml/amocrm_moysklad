import requests

POST = 'POST'
GET = 'GET'
PUT = 'PUT'
DELETE = 'DELETE'
HTTP_CODE_SUCCESS = [200, 201, 307, 303]
URI = 'https://online.moysklad.ru/api/remap/1.1'


class HttpException(Exception):
    pass


class HttpClient:
    def __init__(self, login, password):
        self._session = requests.Session()
        self._session.auth = (login, password)

    def send(self, method, endpoint, parameters=None, payload=None):
        response = self._session.request(
            method,
            url=URI + endpoint,
            headers={
                'Content-Type': 'application/json'
            },
            params=parameters,
            json=payload
        )
        if response.status_code in HTTP_CODE_SUCCESS:
            return response.json()

        if response.status_code == 204:
            return {}

        raise HttpException(response.text)
