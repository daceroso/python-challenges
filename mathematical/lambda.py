# lambda parameter(s): expression

add_one = lambda x: x + 1
double_it = lambda x: x * 2
mult = lambda a, b: a * b
power_of = lambda x, y: x ** y

print(double_it(7))
print(power_of(2, 8))

numbers = [11, 2, 30, 333, 14, 4444, 100, 222]
# numbers.sort()
# numbers.sort(key=lambda x: len(str(x)))
numbers.sort(key=lambda x: (len(str(x)), x))
print(numbers)
