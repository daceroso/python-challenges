even = [n for n in range(10) if n % 2 == 0]
print(even)

with_tuples = [(x,y) for x in range(3) for y in range(5)]
print(with_tuples)

with_tuples_3 = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(with_tuples_3)