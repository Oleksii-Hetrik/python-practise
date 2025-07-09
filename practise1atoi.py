class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1  # 1 for positive, -1 for negative
        result = 0

        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # If we reached the end of the string, or no non-whitespace characters found
        if i == n:
            return 0

        # Step 2: Determine signedness
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Step 3: Conversion
        # Read digits until a non-digit character or end of string is reached
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1

        # Step 4: Rounding (Clamping)
        # Define 32-bit signed integer range
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if sign == 1:
            if result > INT_MAX:
                return INT_MAX
        else:  # sign == -1
            if -result < INT_MIN:
                return INT_MIN

        return result * sign

# Приклади використання:
solver = Solution()

s1 = "42"
print(f"Input: '{s1}' -> Output: {solver.myAtoi(s1)}")  # Output: 42

s2 = "   -042"
print(f"Input: '{s2}' -> Output: {solver.myAtoi(s2)}")  # Output: -42

s3 = "1337c0d3"
print(f"Input: '{s3}' -> Output: {solver.myAtoi(s3)}")  # Output: 1337

s4 = "0-1"
print(f"Input: '{s4}' -> Output: {solver.myAtoi(s4)}")  # Output: 0

s5 = "words and 987"
print(f"Input: '{s5}' -> Output: {solver.myAtoi(s5)}")  # Output: 0

s6 = "-91283472332"
print(f"Input: '{s6}' -> Output: {solver.myAtoi(s6)}")  # Output: -2147483648 (INT_MIN)

s7 = "91283472332"
print(f"Input: '{s7}' -> Output: {solver.myAtoi(s7)}")  # Output: 2147483647 (INT_MAX)

s8 = ""
print(f"Input: '{s8}' -> Output: {solver.myAtoi(s8)}")  # Output: 0

s9 = "  +  413"
print(f"Input: '{s9}' -> Output: {solver.myAtoi(s9)}")  # Output: 0 (because of "  +  ")