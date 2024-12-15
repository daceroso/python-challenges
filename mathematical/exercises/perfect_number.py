def calc_perfect_number(max_exclusive):
    list_perfect_number = []
    for i in range(1, max_exclusive):
        divisors = find_proper_divisor(i)
        sum_divisors = sum_div(divisors)
        perfect_number = is_perfect_number(i, sum_divisors)
        if perfect_number:
            list_perfect_number.append(i)
    return list_perfect_number



def find_proper_divisor(value):
    return [i for i in range(1, value // 2 + 1) if value % i == 0]


def sum_div(value):
    return sum(value)


def is_perfect_number(value, sum_of_divisors):
    return value == sum_of_divisors


def is_perfect_number_simple(number):
    sum_of_multipliers = 1

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            sum_of_multipliers += i
    return sum_of_multipliers == number


print(is_perfect_number_simple(28))


def calc_perfect_numbers(max_exclusive):
    results = []

    for i in range(2, max_exclusive):
        if is_perfect_number_simple(i):
            results.append(i)
    return results


print(calc_perfect_numbers(1000))

print(calc_perfect_number(28))



# list comprehensions

def calc_perfect_number_comprehension(max_exclusive):
    return [i for i in range(2, max_exclusive) if is_perfect_number_simple(i)]

print(calc_perfect_number_comprehension(1000))