strange_message = "a message containing only a message"

mid_chars = strange_message[10:20]

last_seven_chars = strange_message[-7:]

print("mid_chars: ", mid_chars, " / last_seven_chars:", last_seven_chars)

first_char = strange_message[0]
print(first_char, "count:", strange_message.count(first_char))
print(last_seven_chars, "count: ", strange_message.count(last_seven_chars))

# search and cotinue searching

# returns index
print("find message:", strange_message.find("message"))
print("find next message:", strange_message.find("message", 3))

# replace (all)

print("replace by info: ", strange_message.replace("message", "info"))

