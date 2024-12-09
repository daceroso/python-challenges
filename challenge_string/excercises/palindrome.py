def reverse_string(text):
    result = ""
    for current_char in range(len(text) - 1, -1, -1):
        result += text[current_char]
    return result


_text = "Hello"
#
# print(reversed_text)
_reversed_text = "".join(reversed(_text))


def is_palindrome_reverse(text):
    return text.lower() == reverse_string(text).lower()


def is_palindrome(text):
    reversed_text = text[::-1]  # crea una nueva version
    print(reversed_text)
    if text.lower() != reversed_text.lower():
        return False
    return True


def is_palindrome_simple(text):
    return text.lower() == text[::-1].lower()


print(is_palindrome(""))
print(is_palindrome_reverse("Otto"))
print(is_palindrome_reverse("ABCXCV"))
