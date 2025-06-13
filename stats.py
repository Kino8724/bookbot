def get_word_count(text_from_book):
    words = text_from_book.split()
    word_count = len(words)
    return word_count


def get_character_count(text_from_book):
    # Convert all text to lowercase
    lowercase_text = text_from_book.lower()

    characters = {}

    # Loop through each character in text
    for char in lowercase_text:
        # Check if character is a key in the dictionary
        # If character is a key already increment the count value
        if char in characters:
            characters[char] += 1
        # If not a key, create a key for that character, set value to 1
        else:
            characters[char] = 1
    return characters


def sort_on(dict):
    return dict["num"]


def dictionary_to_sorted_list(dictionary):
    list_of_dictionaries = []
    # Loop through the big dictionary
    for key in dictionary:
        # Create a new dictionary for each key value pair
        new_dict = {}
        new_dict["char"], new_dict["num"] = key, dictionary[key]
        # Append the new dict to the list
        list_of_dictionaries.append(new_dict)

    # Sort the list of dictionaries by value from big to small
    list_of_dictionaries.sort(key=sort_on, reverse=True)
    return list_of_dictionaries
