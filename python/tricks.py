items = [
    {
        'per_unit': 10,
        'val': 1,
        'wt': 1,
    },
    {
        'per_unit': 30,
        'val': 3,
        'wt': 3,
    },
    {
        'per_unit': 20,
        'val': 2,
        'wt': 2,
    },
    {
        'per_unit': 4,
        'val': 0,
        'wt': 0,
    }
]

# sort using key 'per_unit'
items.sort(key=lambda x: x['per_unit'])
print(items)