def remove_duplicates(text):
    duplicate = set()
    result = ""
    normalized_letters = text.lower()

    for i, current_char in enumerate(normalized_letters):
        if current_char.isalpha():
            if current_char not in duplicate:
                result += text[i]
                print(result)
                duplicate.add(current_char)
    return result



