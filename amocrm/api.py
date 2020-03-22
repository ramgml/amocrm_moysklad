from amocrm.entities import ProductsCatalog
from amocrm.http_client import HttpClient, POST, GET
from amocrm.serializers import serialize_entity


class AmoCrm:
    def __init__(self, url, login, api_key):
        self.http_client = HttpClient(url)
        self.http_client.auth(login, api_key)

    def add(self, entities):
        if not isinstance(entities, list):
            entities = [entities]
        request = {
            'add': [serialize_entity(entity) for entity in entities]
        }

        response = self.http_client.send(POST, self._get_entity_type(entities), payload=request)

        return prepare_response(response)

    def update(self, entities):
        if not isinstance(entities, list):
            entities = [entities]
        request = {
            'update': [serialize_entity(entity) for entity in entities]
        }

        response = self.http_client.send(POST, self._get_entity_type(entities), payload=request)

        return prepare_response(response)

    def list(self, entity, **kwargs):
        """
        :param entity класс сущности, список которых мы хотим получить

        :param limit_rows	Кол-во выбираемых строк (системное ограничение 500)

        :param limit_offset	Сдвиг выборки (с какой строки выбирать). Работает, только при условии, что limit_rows тоже
        указан

        :param id Выбрать элемент с заданным ID (Если указан этот параметр, все остальные игнорируются).
        Можно передавать в виде массива состоящий из нескольких ID

        :param query Поисковый запрос (Осуществляет поиск по заполненым полям сущности)

        :param responsible_user_id Дополнительный фильтр поиска, по ответственному пользователю
        (Можно передавать в виде массива)

        :param with	Если в параметре with указать значения (список см. здесь), в ответ придёт информация о сделке
        по соответствующему значению.

        :param status	Фильтр по ID статуса сделки (Как узнать список доступных ID см. здесь)
        (Можно передавать в виде массива)

        :param filter/date_create/	Выбрать сделки по дате создания (нужно передавать массив с параметрами from, to)

        :param filter/date_modify/	Выбрать сделки по дате изменения (нужно передавать массив с параметрами from, to)

        :param filter/tasks	Выбрать сделки без задач – 1, сделки с невыполенными задачами – 2

        :param filter/active	Выбрать все активные сделки – 1
        """
        filters = kwargs.get('filter')

        if filters is not None:
            del kwargs['filter']
            kwargs.update(build_filters(filters, 'filter'))

        response = self.http_client.send(GET, entity_type=entity.type, parameters=kwargs)

        if entity == ProductsCatalog:
            return response

        return prepare_response(response)

    def delete(self, entities):
        if not isinstance(entities, list):
            entities = [entities]
        request = {
            'delete': [entity.id for entity in entities]
        }

        return self.http_client.send(POST, self._get_entity_type(entities), payload=request)

    @staticmethod
    def _get_entity_type(entities):
        if len(entities) < 1:
            raise Exception('Too few entities for send')

        return entities[0].type


def build_filters(filters, prefix=''):
    result = {}
    for key, value in filters.items():
        if isinstance(value, dict):
            sub_obj = build_filters(value)
            for sub_key, sub_value in sub_obj.items():
                result[f'{prefix}[{key}]{sub_key}'] = sub_value
        else:
            result[f'{prefix}[{key}]'] = value
    return result


def prepare_response(response):
    items = []
    embedded = response.get('_embedded')
    if embedded is not None:
        items = embedded.get('items') or []
    return items
