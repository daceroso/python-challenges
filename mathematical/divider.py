def find_proper_divisors(value):
    divisors = [1]

    for i in range(2, value // 2 + 1):
        if value % i == 0:
            divisors.append(i)

    return divisors


def _find_proper_divisors(value):
    return [i for i in range(1, value // 2 + 1) if value % i == 0]

print(find_proper_divisors(6))
print(_find_proper_divisors(24))