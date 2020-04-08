from amocrm.entities import BaseEntity


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
