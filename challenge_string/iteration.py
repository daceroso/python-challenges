message = "Python has several loop variants"

for i in range(len(message)):
    print(i, message[i], end=',')
print()
for i, current_char in enumerate(message):
    print(i, current_char, end=',')
print()
for current_char in message:
    print(current_char, end=',')
print()
