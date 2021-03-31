
# Import types and enums
from src.types import product, store
from src.enums import enums

# Create each one of the objects
stv = product.Product(id="stv",
                     name="Sony TV",
                     price=549.99)

cac = product.Product(id="cac",
                     name="Central AC",
                     price=1399.99)

nsh = product.Product(id="nsh",
                     name="Nike Shoe",
                     price=109.50)


mch = product.Product(id="mch",
                     name="Charger",
                     price=30.00)

# Create pricing rules
pricing_rule_1 = {
                     "id": "nsh",
                     "buy": 3,
                     "gain": 2,
                     "condition": ">=",
                     "discount_value": 100.000,
                     "discount_type": enums.DiscountType.BUY_WIN,
                     "gift": None
                 }
pricing_rule_2 = {
                     "id": "stv",
                     "buy": 4,
                     "gain": 0,
                     "condition": ">=",
                     "discount_value": 9.091,
                     "discount_type": enums.DiscountType.PRICE_REDUCTION,
                     "gift": None

}
pricing_rule_3 = {
                     "id": "cac",
                     "buy": 1,
                     "gain": 0,
                     "condition": "==",
                     "discount_value": 0.000,
                     "discount_type": enums.DiscountType.BUY_WIN,
                     "gift": [mch]
                  }

# Put pricing rules in a list
pricing_rules = [pricing_rule_1, pricing_rule_2, pricing_rule_3]

# Create each one of the scenarios
scenario_01 = [nsh, nsh, nsh, mch]
scenario_02 = [nsh, stv, stv, nsh, stv, stv, stv]
scenario_03 = [cac, mch, stv]

# Instance the ConsumerStore object passing pricing rules as parameter
co = store.ConsumerStore(pricing_rules=pricing_rules)

# Add to cart each one of the products in scenarios, print and empty the basket
co.add_to_cart([product for product in scenario_01])
print("Scenario: 01 - Total: $%s - Expected: $249.00" % co.get_total())
co.clean_cart()

co.add_to_cart([product for product in scenario_02])
print("Scenario: 02 - Total: $%s - Expected: $2718.95" % co.get_total())
co.clean_cart()

co.add_to_cart([product for product in scenario_03])
print("Scenario: 03 - Total: $%s - Expected: $1949.98" % co.get_total())
co.clean_cart()

