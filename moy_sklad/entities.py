class Entity:
    entity_name = 'entity'

    def get_fields(self):
        return self.__slots__


class Product(Entity):
    entity_name = 'product'
    __slots__ = (
        "meta",
        "id",
        "accountId",
        "owner",
        "shared",
        "group",
        "version",
        "updated",
        "name",
        "code",
        "externalCode",
        "archived",
        "pathName",
        "uom",
        "minPrice",
        "salePrices",
        "buyPrice",
        "paymentItemType",
        "discountProhibited",
        "country",
        "article",
        "trackingType",
        "weight",
        "volume",
        "barcodes",
        "modificationsCount",
        "isSerialTrackable"
    )


class Counterparty(Entity):
    entity_name = 'counterparty'
    __slots__ = (
        "meta",
        "id",
        "accountId",
        "owner",
        "shared",
        "group",
        "version",
        "updated",
        "name",
        "externalCode",
        "archived",
        "created",
        "companyType",
        "accounts",
        "tags",
        "notes",
        "salesAmount"
    )


class Organization(Entity):
    entity_name = 'organization'
    __slots__ = (
        "meta",
        "id",
        "accountId",
        "owner",
        "shared",
        "group",
        "version",
        "updated",
        "name",
        "externalCode",
        "archived",
        "created",
        "companyType",
        "legalTitle",
        "email",
        "accounts",
        "isEgaisEnable",
        "payerVat",
        "director",
        "chiefAccountant",
        "trackingContractDate"
    )


class CustomerOrder(Entity):
    entity_name = 'customerorder'
    __slots__ = (
        "meta",
        "id",
        "accountId",
        "owner",
        "shared",
        "group",
        "version",
        "updated",
        "name",
        "externalCode",
        "moment",
        "applicable",
        "rate",
        "sum",
        "store",
        "agent",
        "organization",
        "state",
        "documents",
        "created",
        "positions",
        "vatEnabled",
        "vatIncluded",
        "vatSum",
        "payedSum",
        "shippedSum",
        "invoicedSum",
        "reservedSum"
    )
