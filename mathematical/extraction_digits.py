def extract_digits(number):
    remaining_value = number
    while remaining_value > 0:
        digit = remaining_value % 10
        print(digit)
        remaining_value = remaining_value // 10
        print(digit, end=' ')
    print()


print(extract_digits(100))

print(0 % 10)
print(1 % 10)


# built in function

def _extract_digits(number):
    remaining_value = number
    while remaining_value > 0:
        remaining_value, digit = divmod(remaining_value, 10)
        print(digit, end=' ')
    print()

print(_extract_digits(123))
