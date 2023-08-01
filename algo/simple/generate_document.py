def generateDocument(characters, document):
    count_dict = {}
    for char in characters:
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] = count_dict[char] + 1
    for char in document:
        if not char:
            continue
        if char not in count_dict:
            return False
        elif count_dict[char] <= 0:
            return False
        else:
            count_dict[char] -= 1
    return True

