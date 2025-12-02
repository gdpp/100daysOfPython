def manufacture_gifts(gifts_to_produce):
    return [item["toy"] for item in gifts_to_produce for _ in range(item["quantity"]) if item["quantity"] > 0]


production1 = [
    {"toy": 'car', "quantity": 3},
    {"toy": 'doll', "quantity": 1},
    {"toy": 'ball', "quantity": 2}
]

result1 = manufacture_gifts(production1)
print(result1)
# ['car', 'car', 'car', 'doll', 'ball', 'ball']

production2 = [
    {"toy": 'train', "quantity": 0},  # not manufactured
    {"toy": 'bear', "quantity": -2},  # neither
    {"toy": 'puzzle', "quantity": 1}
]

result2 = manufacture_gifts(production2)
print(result2)
# ['puzzle']

production3 = []
result3 = manufacture_gifts(production3)
print(result3)
# []
