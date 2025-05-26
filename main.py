def main():
    # from stats import get_num_words
    # path = "books/frankenstein.txt"
    import sys
    if len(sys.argv) == 1:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path} ...")
    text = get_contents(path)
    # print(text)
    words = num_of_words(text)
    characters = get_characters(text)
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    chars_sorted = report(characters)
    for item in chars_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_contents (path):
    with open(path) as text:
        return text.read()

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

def sort_on(d):
    return d["num"]


def report(characters):
    sorted_list = []
    for ch in characters:
        sorted_list.append({"char": ch, "num": characters[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list    


main ()


