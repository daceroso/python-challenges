from functools import reduce


def join(values, delimiter):
    value = ""
    for i, current_char in enumerate(values):
        value += current_char
        if i < len(values) - 1:
            value += delimiter

    return value



message = ["Hello", "World", "message"]
separator = '-**-'
print(separator.join(message))


def join_with_reduce(values, delimiter):
    return reduce(lambda str1, str2: str1 + delimiter +str2, values)


