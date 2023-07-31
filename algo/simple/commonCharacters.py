def commonCharacters(strings):
    # Write your code here.
    if strings:
        cur_set = set(strings[0])
        for string in strings[1:]:
            cur_set = cur_set.intersection(set(string))
        return list(cur_set)
    return []