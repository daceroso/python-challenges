s = 'seehemewe'
print(s[:3])

print(s[3:5])
print(s[5:7])
print(s[7:])
print(s[3:6])
print(s[5:7] + 'h')
print(s[7:9] + 'e')
print(s[5:2:-1])
print(s[-2::-3])

# single-line expression for determining if a string is a palindrome
print(s == s[::-1])