# Day 2

## Objectives

In this day I learned about:

-   Data types
-   Numbers
-   Operations
-   Type conversion
-   f-String

### Data types

```python
    #String
    "Hello"

    #Integer
    123
    45_567_123

    #float
    3.1415

    #Boolean
    True
    False
```

### Operations

```python
    3 + 5
    7 - 4
    3 * 2
    6 / 3
    2 ** 3 #8

    # PEMDAS
    # Parentheses ()
    # Exponents **
    # Multiplication * & Division /
    # Addition + & Subtraction -
```

## Project of the day

**Tip Calculator**

```python
    print("===================================")
    print("== Welcome to the TIP CALCULATOR ==")
    print("===================================")

    bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
    ppl = int(input("How many people to split the bill? "))

    tip_percent = 1 + tip / 100

    result = round((bill / ppl) * tip_percent, 2)

    print(f"Each person should pay: ${result}")
```

2. Run the script:

```bash
    python tip_calculator.py
```

[Go to Home](../README.md)
