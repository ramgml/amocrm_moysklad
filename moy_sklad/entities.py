class Entity:
    entity_name = 'entity'

    def get_fields(self):
        return self.__slots__


class Product(Entity):
    entity_name = 'product'
    __slots__ = (
        "meta",
        "id",
        "account_id",
        "owner",
        "shared",
        "group",
        "version",
        "updated",
        "name",
        "code",
        "external_code",
        "archived",
        "path_name",
        "uom",
        "min_price",
        "sale_prices",
        "buy_price",
        "payment_item_type",
        "discount_prohibited",
        "country",
        "article",
        "tracking_type",
        "weight",
        "volume",
        "barcodes",
        "modifications_count",
        "is_serial_trackable"
    )


class Counterparty(Entity):
    entity_name = 'counterparty'
    __slots__ = (
        "meta",
        "id",
        "account_id",
        "owner",
        "shared",
        "group",
        "version",
        "updated",
        "name",
        "external_code",
        "archived",
        "created",
        "company_type",
        "accounts",
        "tags",
        "notes",
        "sales_amount"
    )


class Organization(Entity):
    entity_name = 'organization'
    __slots__ = (
        "meta",
        "id",
        "account_id",
        "owner",
        "shared",
        "group",
        "version",
        "updated",
        "name",
        "external_code",
        "archived",
        "created",
        "company_type",
        "legal_title",
        "email",
        "accounts",
        "is_egais_enable",
        "payer_vat",
        "director",
        "chief_accountant",
        "tracking_contract_date"
    )


class CustomerOrder(Entity):
    entity_name = 'customerorder'
    __slots__ = (
        "meta",
        "id",
        "account_id",
        "owner",
        "shared",
        "group",
        "version",
        "updated",
        "name",
        "external_code",
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
        "vat_enabled",
        "vat_included",
        "vat_sum",
        "payed_sum",
        "shipped_sum",
        "invoiced_sum",
        "reserved_sum"
    )
