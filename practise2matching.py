class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if(p == ""):
            if s == "":
                return True
            else:
                return False
        if p[0] == ".":
            if(len(s) > 0):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        if p[0] == "*":
            return self.isMatch(s, p[1:])
        if p[0].isascii():
            if s[0] == p[0]:
                return self.isMatch(s[1:], p[1:])
            else:
                return self.isMatch(s[1:], p)





        # dp[i][j] буде true, якщо перші i символів s збігаються з першими j символів p.
        memo = {}  # Додаємо мемоїзацію для оптимізації рекурсивного рішення

        def dp_match(i, j):
            # Перевіряємо, чи ми вже обчислювали цей стан
            if (i, j) in memo:
                return memo[(i, j)]

            # Базові випадки
            # Якщо обидва рядки досягли кінця, це збіг
            if j == len(p):
                return i == len(s)

            # Якщо рядок s досяг кінця, але p ще ні
            # Це може бути збіг, якщо залишок p виглядає як "a*", "a*b*", тощо
            if i == len(s):
                # Перевіряємо, чи залишок p може бути порожнім
                # Це можливо, якщо він складається з пар "char*"
                if (len(p) - j) % 2 == 1:  # Якщо непарна кількість символів, не може бути збігу
                    return False

                # Перевіряємо, чи всі наступні символи мають бути "*"
                for k in range(j + 1, len(p), 2):
                    if p[k] != '*':
                        return False
                return True

            # Рекурсивні випадки
            first_match = (i < len(s) and (p[j] == s[i] or p[j] == '.'))

            if j + 1 < len(p) and p[j + 1] == '*':
                # Випадок з '*'
                # 1. '*' збігається з нулем входжень попереднього елемента (p[j])
                #    Тоді ми пропускаємо p[j] і p[j+1] (char*)
                # 2. '*' збігається з одним або більше входжень попереднього елемента (p[j])
                #    Тоді поточний символ s[i] збігається з p[j], і ми переходимо до наступного символу в s, залишаючись на тому ж char* в p
                result = dp_match(i, j + 2) or (first_match and dp_match(i + 1, j))
            else:
                # Випадок без '*'
                # Просто збігаємо поточні символи
                result = first_match and dp_match(i + 1, j + 1)

            # Зберігаємо результат у мемо
            memo[(i, j)] = result
            return result

        return dp_match(0, 0)

# Приклади використання:
solver = Solution()

# Приклад 1: "a" не відповідає "aa"
s1, p1 = "aa", "a"
print(f"s = '{s1}', p = '{p1}' -> Result: {solver.isMatch(s1, p1)}") # Output: False

# Приклад 2: "a*" відповідає "aa" (повторення 'a' один раз)
s2, p2 = "aa", "a*"
print(f"s = '{s2}', p = '{p2}' -> Result: {solver.isMatch(s2, p2)}") # Output: True

# Приклад 3: ".*" відповідає "ab" (нуль або більше будь-яких символів)
s3, p3 = "ab", ".*"
print(f"s = '{s3}', p = '{p3}' -> Result: {solver.isMatch(s3, p3)}") # Output: True

# Додаткові приклади:
s4, p4 = "aab", "c*a*b"
print(f"s = '{s4}', p = '{p4}' -> Result: {solver.isMatch(s4, p4)}") # Output: True (c* = "", a* = "aa")

s5, p5 = "mississippi", "mis*is*p*."
print(f"s = '{s5}', p = '{p5}' -> Result: {solver.isMatch(s5, p5)}") # Output: False

s6, p6 = "ab", ".*c"
print(f"s = '{s6}', p = '{p6}' -> Result: {solver.isMatch(s6, p6)}") # Output: False

s7, p7 = "aaa", "a*a"
print(f"s = '{s7}', p = '{p7}' -> Result: {solver.isMatch(s7, p7)}") # Output: True

s8, p8 = "aaa", "ab*a*c*a"
print(f"s = '{s8}', p = '{p8}' -> Result: {solver.isMatch(s8, p8)}") # Output: True