def isPalindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def caesarCipherEncryptor(string, key):
    # Write your code here.
    char_2_idx = {c: i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
    idx_2_char = {i: c for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
    return "".join([idx_2_char[(char_2_idx[c] + key) % 26] for c in string])


def runLengthEncoding(string):
    if not string:
        return ""
    ans_list = []
    cur_char = string[0]
    cur_count = 1
    for c in string[1:]:
        if c == cur_char:
            cur_count += 1
        else:
            ans_list.append(f"{cur_count}{cur_char}")
            cur_char = c
            cur_count = 1
        if cur_count == 10:
            ans_list.append(f"{cur_count - 1}{cur_char}")
            cur_count = 1
    ans_list.append(f"{cur_count}{cur_char}")
    return "".join(ans_list)


def generateDocument(characters, document):
    # Write your code here.
    counter = {}
    for c in characters:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    for c in document:
        if c not in counter or counter[c] == 0:
            return False
        counter[c] -= 1
    return True


def firstNonRepeatingCharacter(string):
    counter = {}
    for c in string:
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1
    for idx, c in enumerate(string):
        if counter[c] == 1:
            return idx
    return -1


def semordnilap(words):
    # Write your code here.
    d = {}
    for word in words:
        key = "".join(sorted(word))
        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]
    return [value for key, value in d.items() if len(value) > 1]

