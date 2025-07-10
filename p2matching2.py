def isMatch(s: str, p: str) -> bool:
    # Create a DP table with dimensions (len(s)+1) x (len(p)+1)
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    # Empty string matches empty pattern
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c* that can match an empty string
    for j in range(2, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # Two cases: zero of the preceding char or one/more
                dp[i][j] = dp[i][j - 2]  # zero
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[len(s)][len(p)]

print(isMatch("aa", "a"))    # False
print(isMatch("aa", "a*"))   # True
print(isMatch("ab", ".*"))   # True

print(isMatch("mississippi", "mis*is*p*.")) # should be true(there is clearly "mis" than "is" and then . - any charchter in the end) but we get false
print(isMatch("aaa", "ab*a*c*a")) # should be false(clearly there is no b or c symbols our actual string is even smaller than pattern) but we get true
