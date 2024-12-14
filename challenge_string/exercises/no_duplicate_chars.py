def check_no_duplicate_chars_dicc(text):
    duplicate = {}
    char_lower = text.lower()
    for current_char in char_lower:
        if current_char.isalpha():
            if current_char in duplicate:
                duplicate[current_char] += 1
                return False
            else:
                duplicate[current_char] = 1
    return True


def check_no_duplicate_chars(text):
    duplicate = set()
    for current_char in text.lower():
        if current_char.isalpha():
            if current_char in duplicate:
                return False
        duplicate.add(current_char)
    return True
