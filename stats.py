def num_of_words (text):
    words = text.split()
    return len(words)

def get_characters(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters
