from moy_sklad.entities import Entity


def serialize_entity(entity: Entity):
    result = {}
    for field in entity.get_fields():
        value = getattr(entity, field, None)
        if value is None:
            continue
        result[to_camelcase(field)] = value
    return result


def to_camelcase(name: str):
    words = name.split('_')
    titled = [word.title() for word in words[1:]]
    return ''.join([words[0].lower()] + titled)
