def firstNonRepeatingCharacter(string):
    # Write your code here.
    count_dict = {}
    for char in string:
        if char not in count_dict:
            count_dict[char] = 0
        count_dict[char] += 1
    for i,char in enumerate(string):
        if count_dict[char] == 1:
            return i
    return -1
