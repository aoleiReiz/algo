def semordnilap(words):
    word_dict = {}
    for word in words:
        word_key = "".join(sorted(list(set(word))))
        if word_key not in word_dict:
            word_dict[word_key] = []
        word_dict[word_key].append(word)

    return [value for value in word_dict.values() if len(value) > 1]


print(semordnilap(["abcdefghijk", "aaa", "hello", "racecar", "kjihgfedcba"]))