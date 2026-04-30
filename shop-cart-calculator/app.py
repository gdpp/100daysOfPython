from utils import apply_discount, calculate_subtotal, calculate_tax, calculate_total

cart = [
    {"name": "Keyboard", "price": 50, "qty": 2},
    {"name": "Mouse", "price": 25, "qty": 1},
    {"name": "Monitor", "price": 300, "qty": 1},
    {"name": "RAM", "price": 2500, "qty": 2},
    {"name": "SSD", "price": 1000, "qty": 1},
    {"name": "Intel Core i7", "price": 4000, "qty": 1},
]


def main():
    subtotal = calculate_subtotal(cart)
    tax = calculate_tax(subtotal)

    print(f"** Subtotal: {subtotal}")
    print(f"** Tax: {tax}")

    total = subtotal + tax

    discount = apply_discount(total, 20)

    print(f"** Disconut: {discount}")

    result = calculate_total(total, discount)

    print(f"** Result: {result} **")


if __name__ == "__main__":
    main()
