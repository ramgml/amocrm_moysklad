from moy_sklad.entities import Entity


def serialize_entity(entity: Entity):
    result = {}
    for field in entity.get_fields():
        value = getattr(entity, field, None)
        if value is None:
            continue
        result[field] = value
    return result
