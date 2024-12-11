# not optimal variant

def remove_all_inplace(list, value):
    try:
        while True:
            list.remove(value)
    except(ValueError):
        pass


print(remove_all_inplace([1, 2, 3, 45, 5], 1))


def remove_all_inplace_improved(values, item):
    while item in values:
        values.remove(item)
