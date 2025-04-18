# List Comprehension and the NATO Alphabet (Day 26)

## List Comprehension

Creates lists concisely using:

```python
    [expression for item in iterable if condition]
```

### Examples

Basic: `[x**2 for x in range(5)]` → `[0, 1, 4, 9, 16]`
With Condition: `[x**2 for x in range(5) if x % 2 == 0]` → `[0, 4, 16]`
Nested: flattened = `[num for row in [[1, 2], [3, 4]] for num in row]` → `[1, 2, 3, 4]`

## Dictionary Comprehension

Creates dictionaries using:

```python
    {key: value for item in iterable if condition}
```

### Examples

Basic: `{x: x**2 for x in range(5)}` → `{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}`
With Condition: `{x: x**2 for x in range(5) if x % 2 == 0}` → `{0: 0, 2: 4, 4: 16}`
From Lists: `{k: v for k, v in zip(['a', 'b'], [1, 2])}` → `{'a': 1, 'b': 2}`

## Best Practices

1. Keep simple for clarity.
2. Use loops for complex logic.
3. Choose descriptive variable names.
4. Performance
5. Comprehensions are often faster than loops for small datasets.
