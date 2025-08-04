class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Крок 1: Обробка базових випадків
        if num1 == "0" or num2 == "0":
            return "0"

        # Довжини чисел
        len1 = len(num1)
        len2 = len(num2)

        # Крок 2: Ініціалізація масиву для результату
        # Максимальна довжина результату = len1 + len2
        # result[i+j] відповідає позиції для поточного добутку
        # result[i+j+1] для переносу
        result = [0] * (len1 + len2)

        # Крок 3: Виконання множення
        # Ітеруємо по num1 та num2 з кінця до початку
        for i in range(len1 - 1, -1, -1):
            digit1 = int(num1[i])  # Перетворюємо символ на цифру

            for j in range(len2 - 1, -1, -1):
                digit2 = int(num2[j])  # Перетворюємо символ на цифру

                # Позиції для поточного добутку
                # pos1 - це розряд одиниць для поточного добутку
                # pos2 - це розряд десятків (переносу) для поточного добутку
                pos1 = i + j + 1
                pos2 = i + j

                # Обчислюємо добуток поточних цифр + будь-який існуючий carry на pos1
                prod = digit1 * digit2 + result[pos1]

                # Одиниці добутку йдуть на pos1
                result[pos1] = prod % 10
                # Десятки добутку (carry) йдуть на pos2
                result[pos2] += prod // 10

        # Крок 4: Форматування результату
        # Перетворюємо список цифр на рядок
        # Видаляємо ведучі нулі (якщо є)
        # Спочатку знаходимо перший ненульовий елемент

        # Знаходимо початок результату (перший ненульовий символ)
        start_index = 0
        while start_index < len(result) - 1 and result[start_index] == 0:
            start_index += 1

        # З'єднуємо цифри в рядок
        return "".join(map(str, result[start_index:]))

# Приклади використання:
solver = Solution()

num1_ex1, num2_ex1 = "2", "3"
print(f"Input: num1 = '{num1_ex1}', num2 = '{num2_ex1}' -> Output: '{solver.multiply(num1_ex1, num2_ex1)}'") # Expected: "6"

num1_ex2, num2_ex2 = "123", "456"
print(f"Input: num1 = '{num1_ex2}', num2 = '{num2_ex2}' -> Output: '{solver.multiply(num1_ex2, num2_ex2)}'") # Expected: "56088"

num1_ex3, num2_ex3 = "0", "0"
print(f"Input: num1 = '{num1_ex3}', num2 = '{num2_ex3}' -> Output: '{solver.multiply(num1_ex3, num2_ex3)}'") # Expected: "0"

num1_ex4, num2_ex4 = "9", "9"
print(f"Input: num1 = '{num1_ex4}', num2 = '{num2_ex4}' -> Output: '{solver.multiply(num1_ex4, num2_ex4)}'") # Expected: "81"

num1_ex5, num2_ex5 = "99", "99"
print(f"Input: num1 = '{num1_ex5}', num2 = '{num2_ex5}' -> Output: '{solver.multiply(num1_ex5, num2_ex5)}'") # Expected: "9801"

num1_ex6, num2_ex6 = "1", "1"
print(f"Input: num1 = '{num1_ex6}', num2 = '{num2_ex6}' -> Output: '{solver.multiply(num1_ex6, num2_ex6)}'") # Expected: "1"

num1_ex7, num2_ex7 = "123456789", "987654321"
print(f"Input: num1 = '{num1_ex7}', num2 = '{num2_ex7}' -> Output: '{solver.multiply(num1_ex7, num2_ex7)}'") # Expected: "121932631112635269"