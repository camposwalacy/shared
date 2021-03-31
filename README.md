# Technical test

---

## 1 - Problem Solving
--- ---
To solve the problem of ConsumerStore I chosed to built some structure in terms of project, like:
```
-- cargill-dev
    README.md (this file)
    -- src
        test.py
        -- enums
            enums.py
        -- types
            product.py
            store.py
```
Each of these files represents part of the solution to isolate responsabilities, according to POO.

| File | Description |
| ----------- | ----------- |
| README.md | This tutorial and a documentation for classes |
| test.py | Where the tests can be runed |
| enums.py | Enums types for the classes among solution |
| product.py | Represents the product class |
| store.py | Represents the store class |
Table 01 - Descriptions of classes



### 1.1 - Prerequisites
The execute only requeres python version 3.8+, which this activity has been built in.

### 1.2 - How to build objects
To declare new objects, there is some important informations we need to fill.

To declare a product:
```
# Import types and enums
from src.types import product, store
from src.enums import enums

# Create each one of the objects
stv = product.Product(id="stv",
                     name="Sony TV",
                     price=549.99)
```
Where the **id** of product is unique, so the another Sony TVs might have the same **id**.
The **name** and **price** are necessary to creation of this object.

To declare a new rule:
```
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
```
This structure is very important to make rules available in ConsumerStore.
The id represents the **id** of product. The rule will be aplied for the group of products which has the same **id**.

The **buy** variable represents the value of items that has been necessary to reach.

The **gain** represents how many items could be gained based on **buy**.

The **condition** represents which condition has to be satisfied to make the pricing rule real.
We can see it in table 02.

The **discount_value** is a value in percentage in the interval of 0 to 100. 
The decimal houses has to be precised with more than 2.

The **discount_type** is a enumerate typo to help to filter which type of discount we are applying on.
If we want to make roles like "Buy 3 and Win 2", we have to choose **BUY_WIN**. If our goal is just to apply 
a significant discount value, we use **PRICE_REDUCTION**.

Last, but not least, the **gift** fields represents what this offer should retrieve as a gift.

To illustrate that, let's explore the rule 01.

"1. We have a 3 for 2 great deal on Nike Shoes. i.e. if you buy 3 Nike Shoes, you’ll just pay the price of 2."

So, our **buy** value has to be 3, because the consumer has to buy at least 3 pairs of Nike Shoes.
Our gain will be 2, because we are only going to pay for two pairs of Nike Shoes.
To satisfy our condition, our **condition** field has to be **>=**, because we want to have more or equal 3.
Our **discount_value** will be 100, because we win 1 pair of Nike Shoes in this rule.
To our **discount_type**, it is a **BUY_WIN** rule.
To the **gift** field we have nothing, because there is no gift of this rule.

The whole info about how does variables works are also located in the code for each of the classes.

The table with **condition** operators is on table 02, on next:

| Operator | Description |
| ----------- | ----------- |
| == | Equal |
| != | Different |
| \> | Higher than |
| >= | Higher or equal than |
| < | Lower than |
| <= | Lower or equal than |
Table 02 - Descriptions of operators for condition field in pricing rules

Note that I use the same logical operators that Python language uses.


To declare a consumer store:

```
co = store.ConsumerStore(pricing_rules=pricing_rules)
```
Where the **pricing_rules** can be represented as **pricing_rule_1**.

### 1.3 - How to execute
To execute the tests of the exercise goes to [/cargill-dev/src/](/cargill-dev/src/) and runs:
```
python test.py
```


### 1.4 - Results
The results will be shown on python console. Showing the Total, which is calculates by the program, 
and the expected value from the exercise.

---
    30/03/2021

    author: Walacy da Silva Campos
    email: camposwalacy@gmail.com
---