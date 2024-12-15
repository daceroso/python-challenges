

def number_as_text(n):
    value_to_text = ""

    while n > 0:
        remainder = n % 10

        if remainder == 0:
            value_to_text = "ZERO" + " " + value_to_text
        if remainder == 1:
            value_to_text = "ONE" + " " + value_to_text

        if remainder == 2:
            value_to_text = "TWO" + " " + value_to_text

        if remainder == 3:
            value_to_text = "THREE" + " " + value_to_text

        if remainder == 4:
            value_to_text = "FOUR" + " " + value_to_text

        if remainder == 5:
            value_to_text = "FIVE" + " " + value_to_text

        if remainder == 6:
            value_to_text = "SIX" + " " + value_to_text

        if remainder == 7:
            value_to_text = "SEVEN" + " " + value_to_text

        if remainder == 8:
            value_to_text = "EIGHT" + " " + value_to_text

        if remainder == 9:
            value_to_text = "NINE" + " " + value_to_text

        n = n // 10
    return value_to_text


print(number_as_text(42))
print(number_as_text(456))

print(456 % 10)
print(456 // 10)