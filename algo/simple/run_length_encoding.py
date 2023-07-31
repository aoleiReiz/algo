def runLengthEncoding(string):
    # Write your code here.
    curr_char = ""
    curr_count = 0
    ans = []
    for char in string:
        if curr_char != char:
            if curr_count > 0:
                ans.append(f"{curr_count}{curr_char}")
                curr_count = 1
                curr_char = char
            else:
                curr_char = char
                curr_count = 1
        else:
            curr_count += 1
            if curr_count == 10:
                ans.append(f"9{curr_char}")
                curr_count = 1
    if curr_count > 0:
        ans.append(f"{curr_count}{curr_char}")
    return "".join(ans)