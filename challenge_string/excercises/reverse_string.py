def reverse_string(text):
    result = ""
    for current_char in range(len(text) - 1, -1, -1):
        result += text[current_char]
    return result
