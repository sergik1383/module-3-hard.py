def calculate_structure_sum(obj):
    total = 0
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return len(obj)
    elif isinstance(obj, dict):
        obj = list(obj.items())
    for value in obj:
        total += calculate_structure_sum(value)
    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
