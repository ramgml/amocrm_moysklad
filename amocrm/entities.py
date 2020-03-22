class BaseEntity(object):
    def get_fields(self):
        return self.__slots__

    def __repr__(self):
        fields = ((field, getattr(self, field)) for field in dir(self))
        return '\n'.join((f'{key}: {str(value)}' for key, value in fields))


class Lead(BaseEntity):
    type = 'leads'
    __slots__ = (
        'id',
        'name',
        'responsible_user_id',
        'created_at',
        'updated_at',
        'status_id',
        'pipeline_id',
        'sale',
        'tags',
        'contacts_id',
        'company_id',
        'custom_fields',
        'catalog_elements_id',
        'unlink'
    )


class ProductsCatalog(BaseEntity):
    type = 'products_settings'
    __slots__ = (
        'is_enabled',
        'catalog_id'
    )


class CatalogElement(BaseEntity):
    type = 'catalog_elements'
    __slots__ = (
        'id',
        'catalog_id',
        'name',
        'custom_fields',
        'created_at',
        'updated_at'
    )


class CustomField(BaseEntity):
    __slots__ = (
        'id'
    )

    type = 'custom_fields'

    def __init__(self):
        self._values = None

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        if isinstance(value, str) or isinstance(value, int) or isinstance(value, bool):
            self._values = [{'value': value}]
        else:
            self._values = value

    def get_fields(self):
        slots = list(self.__slots__)
        return tuple(slots + ['values'])
