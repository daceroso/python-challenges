def reverse_string(text):
    result = ""
    for current_char in range(len(text) - 1, -1, -1):
        result += text[current_char]
    return result


text = "Hello"
reversed_text = text[::-1]
_reversed_text = "".join(reversed(text))

