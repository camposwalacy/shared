from src.enums.enums import DiscountType

class ConsumerStore():
    def __init__(self, pricing_rules):
        """
        This class refers to a CosumerStore where products can be bought
        :param pricing_rules: (dict) Pricing rules of ConsumerStore
        """
        self.shopping_cart = []
        self.pricing_rules = pricing_rules

    def add_to_cart(self, item):
        """
        This function adds one or more items to cart
        :param item: (list) or (Product object)
        :return: None
        """
        if (type(item) == list):
            self.shopping_cart += item
        else:
            self.shopping_cart.append(item)

    def remove_from_cart(self, item):
        """
        This function remove one or more items from cart
        :param item: (list) or (Product object)
        :return: None
        """
        if (type(item) == list):
            for i in item:
                self.shopping_cart.remove(i)
        else:
            self.shopping_cart.remove(item)

    def clean_cart(self):
        """
        This function removes all items from the cart
        :return: None
        """
        self.shopping_cart = []

    def _calculate_discount(self, item_value, discount_percentage):
        """
        Calculate discount for each item based on the rules
        :param item_value: (float) The value of item
        :param discount_percentage: (float) Percentage of discount for that item
        :return: (float) The value of discount for that item
        """
        return ((discount_percentage * item_value) / 100)

    def apply_discount(self, total):
        """
        Applies discount on total value
        :param total: (float) Sum of every item in the cart
        :return: (float) The total value of cart sum
        """
        #Get unique item ids
        ids = list(set([sc.id for sc in self.shopping_cart]))

        #Iter among every id
        for id in ids:

            #Get a grouped items based on id
            group = [c for c in self.shopping_cart if c.id == id]

            #Iter among pricing rules
            for pr in self.pricing_rules:

                if (pr["id"] == id):

                    item_price = group[0].price
                    discount_type = pr["discount_type"]
                    condition = pr["condition"]
                    buy = pr["buy"]
                    gain = pr["gain"]
                    gift = pr["gift"]
                    discount = pr["discount_value"]
                    gained_items = 0
                    value = 0

                    if(discount_type == DiscountType.BUY_WIN and gain >= 1):
                        gained_items = len(group) / buy

                    elif(discount_type == DiscountType.PRICE_REDUCTION):
                        if (condition == "=="):
                            if (len(group) == buy):
                                value = sum([self._calculate_discount(item_value=g.price,
                                                                      discount_percentage=discount) for g in group])

                        elif (condition == "!="):
                            if (len(group) != buy):
                                value = sum([self._calculate_discount(item_value=g.price,
                                                                      discount_percentage=discount) for g in group])

                        elif (condition == ">"):
                            if(len(group) > buy):
                                value = sum([self._calculate_discount(item_value=g.price,
                                                                      discount_percentage=discount) for g in group])

                        elif (condition == ">="):
                            if (len(group) >= buy):
                                value = sum([self._calculate_discount(item_value=g.price,
                                                                      discount_percentage=discount) for g in group])

                        elif (condition == "<"):
                            if (len(group) < buy):
                                value = sum([self._calculate_discount(item_value=g.price,
                                                                      discount_percentage=discount) for g in group])

                        elif (condition == "<="):
                            if (len(group) <= buy):
                                value = sum([self._calculate_discount(item_value=g.price,
                                                                      discount_percentage=discount) for g in group])

                        else:
                            pass

                    value = (item_price * gained_items) if gained_items >= 1 else value

                    if(gift != None):
                        if(type(gift) == list):
                            value = sum([g.price for g in gift])
                        else:
                            value = gift.price

                        self.add_to_cart(gift)

                    total -= value





        return total

    def get_total(self):
        """
        This function gets the sum of items in the cart
        :return: (float) Sum value of total items in cart
        """
        total = sum([item.price for item in self.shopping_cart])

        total_with_discounts = self.apply_discount(total)

        return round(total_with_discounts, 2)





