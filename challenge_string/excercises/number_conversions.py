def is_binary_number(number):
    for char in number:
        if char != '1' and char != '0':
            return False
    return True


def is_binary_number_v2(number):
    for current_char in number:
        if current_char not in ["0", "1"]:
            return False
    return True


def binary_to_decimal(number):
    if not is_binary_number(number):
        raise ValueError(number + " is not a binary number")

    decimal_value = 0
    for current_char in number:
        value = int(current_char)
        decimal_value = decimal_value * 2 + value

    return decimal_value


def hex_to_decimal(number):
    if not is_hex_number(number):
        raise ValueError(number + " is not a hex number")

    hex_value = 0

    for current_char in number:
        if current_char.isdigit():
            value = int(current_char)
        elif 'A' <= current_char <= 'F':
            value = ord(current_char.upper()) - 55

        hex_value = hex_value * 16 + value
    return hex_value


def hex_to_decimal_v2(number):
    if not is_hex_number(number):
        raise ValueError(number + " is not a hex number")

    decimal_value = 0
    for current_char in number:
        if current_char.isdigit():
            value = int(current_char)
        else:
            value = ord(current_char.upper()) - ord("A") + 10

        decimal_value = decimal_value * 16 + value

    return decimal_value


def is_hex_number(number):
    for current_char in number:
        if current_char not in "0123456789ABCDEFabcdef":
            return False

    return True
