class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        negaive_factor = False
        if(dividend < 0 and divisor > 0):
            negaive_factor = True
            dividend = -dividend
        if (divisor < 0 and dividend > 0):
            negaive_factor = True
            divisor = -divisor
        if (divisor < 0 and dividend < 0):
            dividend = -dividend
            divisor = -divisor
        while(True):
            dividend -= divisor
            if dividend >= 0:
                result += 1
            else:
                break
        if negaive_factor:
            result = -result
        return result


    def divideGPT(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        # Обробка особливого випадку переповнення
        # -2^31 / -1 = 2^31, що перевищує INT_MAX
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Визначаємо знак результату
        # Якщо вони мають різні знаки, результат буде від'ємним
        is_negative = (dividend < 0) != (divisor < 0)

        # Працюємо з від'ємними числами, щоб уникнути переповнення,
        # якщо dividend = INT_MIN, оскільки abs(INT_MIN) > INT_MAX
        # Також це спрощує логіку порівняння та віднімання.
        dividend = -abs(dividend)
        divisor = -abs(divisor)  # Тепер обидва від'ємні

        quotient = 0

        # Основний цикл: Віднімаємо дільник від дивіденда
        # Поки dividend >= divisor (для від'ємних чисел, це означає dividend менше або дорівнює divisor по абсолютній величині)
        while dividend <= divisor:
            temp_divisor = divisor
            multiple = 1
            # Внутрішній цикл: Знаходимо найбільшу кратність дільника (divisor * 2^k),
            # яка все ще менше або дорівнює поточному dividend
            # Увага: temp_divisor << 1 може переповнитися, якщо воно стане занадто великим.
            # Для від'ємних чисел, якщо temp_divisor стає меншим за INT_MIN,
            # або при зсуві стає більшим за dividend, ми зупиняємося.
            # умова (temp_divisor >= dividend >> 1) запобігає переповненню temp_divisor
            # до того, як воно стане більшим за dividend,
            # або перетворенню на позитивне (якщо int_min / 2)
            while temp_divisor >= dividend and temp_divisor >= INT_MIN >> 1:  # Додано INT_MIN >> 1 для запобігання переповнення
                # Перевіряємо, чи наступне подвоєння temp_divisor все ще менше або дорівнює dividend
                # (для від'ємних чисел: більше або дорівнює)
                if temp_divisor < dividend - temp_divisor:  # Ця умова перевіряє, чи буде temp_divisor * 2 <= dividend (по абс. знач.)
                    break  # Якщо ні, то поточний temp_divisor - це найбільша можлива кратність

                temp_divisor <<= 1  # Еквівалент temp_divisor *= 2
                multiple <<= 1  # Еквівалент multiple *= 2

            # Віднімаємо знайдену кратність
            dividend -= temp_divisor
            quotient += multiple

        # Застосовуємо знак до результату
        if is_negative:
            quotient = -quotient

        # Перевірка на обмеження 32-бітного цілого числа
        # Це вже оброблено для випадку INT_MIN / -1, тому інші випадки
        # випливають з того, що ми працювали з від'ємними числами.
        # Однак, якщо в процесі обчислень quotient перевищив INT_MAX,
        # його потрібно обрізати.
        if quotient > INT_MAX:
            return INT_MAX
        if quotient < INT_MIN:  # Цей випадок технічно не повинен траплятися з нашою логікою, але для повноти
            return INT_MIN

        return quotient
# Приклади використання:
solver = Solution()

# Приклад 1
dividend1, divisor1 = 10, 3
print(f"Input: dividend = {dividend1}, divisor = {divisor1} -> Output: {solver.divide(dividend1, divisor1)}") # Expected: 3

# Приклад 2
dividend2, divisor2 = 7, -3
print(f"Input: dividend = {dividend2}, divisor = {divisor2} -> Output: {solver.divide(dividend2, divisor2)}") # Expected: -2

# Приклад переповнення (INT_MIN / -1)
dividend3, divisor3 = -2**31, -1
print(f"Input: dividend = {dividend3}, divisor = {divisor3} -> Output: {solver.divide(dividend3, divisor3)}") # Expected: 2147483647 (INT_MAX)

# Інші випадки
dividend4, divisor4 = 0, 1
print(f"Input: dividend = {dividend4}, divisor = {divisor4} -> Output: {solver.divide(dividend4, divisor4)}") # Expected: 0

dividend5, divisor5 = 1, 1
print(f"Input: dividend = {dividend5}, divisor = {divisor5} -> Output: {solver.divide(dividend5, divisor5)}") # Expected: 1

dividend6, divisor6 = -1, 1
print(f"Input: dividend = {dividend6}, divisor = {divisor6} -> Output: {solver.divide(dividend6, divisor6)}") # Expected: -1

dividend7, divisor7 = -2147483648, 2
print(f"Input: dividend = {dividend7}, divisor = {divisor7} -> Output: {solver.divide(dividend7, divisor7)}") # Expected: -1073741824

print("--------------------------------------------------------")

dividend1, divisor1 = 10, 3
print(f"Input: dividend = {dividend1}, divisor = {divisor1} -> Output: {solver.divideGPT(dividend1, divisor1)}") # Expected: 3

# Приклад 2
dividend2, divisor2 = 7, -3
print(f"Input: dividend = {dividend2}, divisor = {divisor2} -> Output: {solver.divideGPT(dividend2, divisor2)}") # Expected: -2

# Приклад переповнення (INT_MIN / -1)
dividend3, divisor3 = -2**31, -1
print(f"Input: dividend = {dividend3}, divisor = {divisor3} -> Output: {solver.divideGPT(dividend3, divisor3)}") # Expected: 2147483647 (INT_MAX)

# Інші випадки
dividend4, divisor4 = 0, 1
print(f"Input: dividend = {dividend4}, divisor = {divisor4} -> Output: {solver.divideGPT(dividend4, divisor4)}") # Expected: 0

dividend5, divisor5 = 1, 1
print(f"Input: dividend = {dividend5}, divisor = {divisor5} -> Output: {solver.divideGPT(dividend5, divisor5)}") # Expected: 1

dividend6, divisor6 = -1, 1
print(f"Input: dividend = {dividend6}, divisor = {divisor6} -> Output: {solver.divideGPT(dividend6, divisor6)}") # Expected: -1

dividend7, divisor7 = -2147483648, 2
print(f"Input: dividend = {dividend7}, divisor = {divisor7} -> Output: {solver.divideGPT(dividend7, divisor7)}") # Expected: -1073741824