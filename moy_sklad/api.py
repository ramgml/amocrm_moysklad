from moy_sklad.http_client import HttpClient, GET, POST, PUT, DELETE
from moy_sklad.serializers import serialize_entity
from moy_sklad.entities import Entity


class MoySklad:
    def __init__(self, login, password):
        self._http_client = HttpClient(login, password)

    def get_assortment(self,
                       limit: int = 100,
                       offset: int = None,
                       stockstore: str = None,
                       stockmoment: str = None,
                       scope: str = None,
                       stockmode: str = None,
                       quantitymode: str = None):
        parameters = {}
        if limit is not None:
            parameters['limit'] = limit
        if offset is not None:
            parameters['offset'] = offset
        if stockstore is not None:
            parameters['stockstore'] = stockstore
        if stockmoment is not None:
            parameters['stockmoment'] = stockmoment
        if scope is not None:
            parameters['scope'] = scope
        if stockmode is not None:
            parameters['quantitymode'] = quantitymode

        return self._http_client.send(GET, f'/entity/assortment', parameters=parameters)

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

    def get_by_id(self, entity_name: str, uuid: str, expand=None):
        parameters = {}
        if expand is not None:
            parameters['expand'] = expand
        return self._http_client.send(GET, f'/entity/{entity_name}/{uuid}', parameters=parameters)

    def add(self, entity: Entity):
        data = serialize_entity(entity)
        return self._http_client.send(POST, f'/entity/{entity.entity_name}', payload=data)

    def update(self, entity: Entity, uuid: str):
        data = serialize_entity(entity)
        return self._http_client.send(PUT, f'/entity/{entity.entity_name}/{uuid}', payload=data)

    def delete(self, entity_name: str, uuid: str):
        return self._http_client.send(DELETE, f'/entity/{entity_name}/{uuid}')
