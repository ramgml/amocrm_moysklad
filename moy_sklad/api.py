from moy_sklad.http_client import HttpClient, GET, POST, PUT, DELETE
from moy_sklad.serializers import serialize_entity
from moy_sklad.entities import Entity


class MoySklad:
    def __init__(self, login, password):
        self._http_client = HttpClient(login, password)

    def get_assortment(self, **kwargs):
        """
        param: limit
        number (optional) Default: 25 Example: 100
        Максимальное количество сущностей для извлечения.

        Допустимые значения 1 - 100

        param: offset
        number (optional) Default: 0 Example: 40
        Отступ в выдаваемом списке сущностей

        param: stockstore
        string (optional)
        Ссылка на склад, по которому нужно получить остатки. Формат - URI.

        param: stockmoment
        string (optional)
        Момент времени, на который нужно вывести остатки.
        Формат строки: YYYY-MM-DD HH:MM:SS.

        param: scope
        string (optional)
        Параметр фильтрации по типу объектов. Принимает одно из значений:

            product - будут выведены только товары
            variant - будут выведены товары и модификации
            consignment - будут выведены все сущности (аналогично отсутствию параметра)


        :param stockmode
        string (optional)
        Вид Остатка. Параметр совместим только с параметрами: limit, offset, stockstore, stockmoment, quantitymode.
        Если указаны параметры отличные от совместимых в ответ вернется ошибка с кодом 1069.
        Допустимые значения [all, positiveOnly, negativeOnly, empty, nonEmpty]
        По умолчанию параметр stockmode имеет значение all. Если вы хотите увидеть объекты с нулевым или отрицательным
        остатком, нужно указать соответствующее значение данного параметра

        :param quantitymode
        string (optional)
        Фильтр по полю Доступно. Параметр совместим только с параметрами: limit, offset, stockstore, stockmoment,
        stockmode. Если указаны параметры отличные от совместимых в ответ вернется ошибка с кодом 1069.
        Допустимые значения [all, positiveOnly, negativeOnly, empty, nonEmpty]
        По умолчанию параметр quantitymode имеет значение all. Если вы хотите увидеть объекты с нулевым или
        отрицательным значением поля Доступно, нужно указать соответствующее значение данного параметра.
        """

        return self._http_client.send(GET, f'/entity/assortment', parameters=kwargs)

    def list(self, entity_name: str, search=None, filters=None, order=None, expand=None):
        parameters = {}
        if search is not None:
            parameters['search'] = search
        if filters is not None:
            parameters['filters'] = filters
        if order is not None:
            parameters['order'] = order
        if expand is not None:
            parameters['expand'] = expand
        return self._http_client.send(GET, f'/entity/{entity_name}', parameters=parameters)

    def get_by_id(self, entity_name: str, uuid, expand=None):
        parameters = {}
        if expand is not None:
            parameters['expand'] = expand
        return self._http_client.send(GET, f'/entity/{entity_name}/{uuid}', parameters=parameters)

    def add(self, entity: Entity):
        data = serialize_entity(entity)
        return self._http_client.send(POST, f'/entity/{entity.entity_name}', payload=data)

    def update(self, entity: Entity, uuid):
        data = serialize_entity(entity)
        return self._http_client.send(PUT, f'/entity/{entity.entity_name}/{uuid}', payload=data)

    def delete(self, entity_name: str, uuid):
        return self._http_client.send(DELETE, f'/entity/{entity_name}/{uuid}')
