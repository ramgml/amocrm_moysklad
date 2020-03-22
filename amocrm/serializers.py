from amocrm.entities import ProductsCatalog, CustomField, BaseEntity


def product_catalog_deserializer(response):
    product_catalog = ProductsCatalog()
    product_catalog.is_enabled = response.get('is_enabled')
    product_catalog.catalog_id = response.get('catalog_id')
    return product_catalog


def serialize_entity(entity: BaseEntity):
    result = {}
    for field in entity.get_fields():
        value = getattr(entity, field, None)
        if value is None:
            continue
        if field == 'custom_fields':
            value = [serialize_entity(custom_field) for custom_field in value]
        result[field] = value

    return result
