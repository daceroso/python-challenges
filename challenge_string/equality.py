str1 = 'String with same contents but different quotes'
str2 = "String with same contents but different quotes"
str3 = "String with same contents but XXX quotes".replace("XXX", "different")

print("str1: ", str1)
print("str2: ", str2)
print("str3: ", str3)

if str1 == str2:
    print("same content")
if str1 is str2:
    print("same reference str1 / str2")
if str1 == str3:
    print("same content")
if str1 is str3:
    print("same reference str1 / str3")
