from enum import Enum

class ProductType(Enum):
    UNKNOWN = 0
    ELECTRONIC = 1
    CLOTHING = 2


class DiscountType(Enum):
    PRICE_REDUCTION = 0
    BUY_WIN = 1
