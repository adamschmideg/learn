def highestValuePalindrome(s, n, k):
    changes_needed = 0
    for i in range(int(len(s) / 2)):
        if s[i] != s[-i - 1]:
            changes_needed += 1
    if changes_needed > k:
        return "-1"
    i = 0
    s = list(s)
    changes = 0
    while changes < (k - changes_needed) and i < len(s) / 2:
        if i == int(len(s) / 2):
            s[i] = '9'
            changes += 1
        elif max(s[i], s[-i - 1]) == '9':
            s[i] = '9'
            s[-i - 1] = '9'
            changes += 1
            changes_needed -= 1
        elif s[i] == s[-i - 1]:
           if k - changes_needed - changes >= 2:
               s[i] = '9'
               s[-i - 1] = '9'
               changes += 2
        else:
            if k - changes_needed - changes >= 1:
                s[i] = '9'
                s[-i - 1] = '9'
                changes += 2
                changes_needed -= 1
        i += 1
    while i <= k and i < len(s) / 2:
        if s[i] != s[-i - 1]:
            v = max(s[i], s[-i - 1])
            s[i] = v
            s[-i - 1] = v
        i += 1
    return "".join(s)

tests = [
    [12321, 1, 12921],
    [12321, 2, 92329],
    [1231, 1, 1331],
    [1234, 1, -1],
    [1234, 2, 4334],
    [1234, 3, 9339],
    [12539, 2, 93539],
]

if __name__ == '__main__':
    for t in tests:
        [num, k, want] = t
        s = str(num)
        got = highestValuePalindrome(s, len(s), k)
        if got != str(want):
            print(f"pali({num}, {k}) == {want}, but got {got}")