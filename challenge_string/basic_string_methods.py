str1 = "DOUBLE QUOTED STRING"
str2 = 'SINGLE QUOTED STRING'

print(str1[::-1])

name = "Carl Heinz Miller"
print(name.lower())
print(name.upper())

print(name.split())

time = '20:26:45'

hrs, mins, sec = time.split(':')
print(hrs, mins, sec)

print("-repeater-" * 3)

with_whitespace = "  --CONTENT--  "
stripped1 = with_whitespace.strip()
stripped2 = stripped1.strip("-")
print("strip1: ", stripped1, "length:", len(stripped1))
print("strip2: ", stripped2, "length:", len(stripped2))
