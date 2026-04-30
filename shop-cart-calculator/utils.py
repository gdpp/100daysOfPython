def calculate_subtotal(cart):
    subtotal = 0

    for item in cart:
        subtotal = subtotal + (item["price"] * item["qty"])

    return subtotal


def calculate_tax(amount, tax=0.16):
    return amount * tax


def apply_discount(amount, discount=0):
    discount_percentage = discount / 100

    return amount * discount_percentage


def calculate_total(amount, discount=0.0):
    return amount - discount
