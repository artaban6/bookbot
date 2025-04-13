def get_num_of_words(text):
    count = 0
    num_of_words = text.split()
    for word in num_of_words:
        count += 1
    return count
    # return print(f"{count} words found in the document")


def get_num_of_characters(text):
    num_of_characters = {}
    characters = text.lower()
    for character in characters:
        if character not in num_of_characters:
            num_of_characters[character] = 1
        elif character in num_of_characters:
            num_of_characters[character] += 1
    return num_of_characters


def get_dict(dict):
    sorted_dict = {k: v for k, v in sorted(
        dict.items(), key=lambda item: item[1], reverse=True)}

    return sorted_dict
