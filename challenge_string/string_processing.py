from operator import itemgetter


def generate_character_histogram(word):
    char_count_map = {}

    for char in list(word.lower()):
        if char.isalpha():
            if char in char_count_map:
                char_count_map[char] = char_count_map[char] + 1
            else:
                char_count_map[char] = 1
    return dict(sorted(char_count_map.items(), key=itemgetter(0)))


word1 = generate_character_histogram("Otto")
print(word1)
word2 = generate_character_histogram("Hello Micha")
print(word2)
word3 = generate_character_histogram("Python Challenges, Your Python Training")
print(word3)
