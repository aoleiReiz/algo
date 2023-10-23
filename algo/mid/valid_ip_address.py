def validIPAddresses(string):
    # Write your code here.
    def is_valid_number(sub_string):
        if sub_string.startswith("0") and len(sub_string) > 1:
            return False
        return  int(sub_string)<= 255 and int(sub_string) >= 0
    def dfs(s, idx, cur, ans):
        if len(cur) == 4 and idx >= len(s):
            ans.append(".".join(cur))
            return
        if idx >= len(s):
            return
        for i in range(1, 4):
            sub_string = s[idx: idx + i]
            if is_valid_number(sub_string) and idx + i <= len(s):
                cur.append(sub_string)
                dfs(s, idx + i, cur, ans)
                cur.pop()
    ans = []
    dfs(string, 0, [], ans)
    return ans
