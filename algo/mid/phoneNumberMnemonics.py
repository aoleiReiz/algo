def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    def helper(idx, cur):
        if idx == len(phoneNumber):
            ans.append("".join(cur))
            return
        for char in number_mapping[phoneNumber[idx]]:
            cur.append(char)
            helper(idx + 1, cur)
            cur.pop()

    ans = []
    number_mapping = {
        "0": "0",
        "1": "1",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    helper(0, [])
    return ans


print(phoneNumberMnemonics("1905"))
