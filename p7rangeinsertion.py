class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Етап 1: Додати всі інтервали, що не перекриваються і знаходяться до newInterval
        # Ми перевіряємо, чи поточний інтервал закінчується до початку newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Етап 2: Об'єднати всі перекриваючі інтервали
        # Перекриття відбувається, коли поточний інтервал починається до того, як newInterval закінчується
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Додати об'єднаний newInterval до результату
        result.append(newInterval)

        # Етап 3: Додати всі решта інтервалів, що не перекриваються і знаходяться після newInterval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


# Приклади використання:
solver = Solution()

# Приклад 1
intervals1 = [[1,3],[6,9]]
newInterval1 = [2,5]
print(f"Input: intervals = {intervals1}, newInterval = {newInterval1} -> Output: {solver.insert(intervals1, newInterval1)}") # Expected: [[1,5],[6,9]]

# Приклад 2
intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval2 = [4,8]
print(f"Input: intervals = {intervals2}, newInterval = {newInterval2} -> Output: {solver.insert(intervals2, newInterval2)}") # Expected: [[1,2],[3,10],[12,16]]

# Приклад 3: Вставка в початок
intervals3 = [[5,7],[9,12]]
newInterval3 = [2,4]
print(f"Input: intervals = {intervals3}, newInterval = {newInterval3} -> Output: {solver.insert(intervals3, newInterval3)}") # Expected: [[2,4],[5,7],[9,12]]

# Приклад 4: Вставка в кінець
intervals4 = [[1,2],[3,4]]
newInterval4 = [5,6]
print(f"Input: intervals = {intervals4}, newInterval = {newInterval4} -> Output: {solver.insert(intervals4, newInterval4)}") # Expected: [[1,2],[3,4],[5,6]]

# Приклад 5: Вставка, що поглинає весь масив
intervals5 = [[1,5]]
newInterval5 = [0,6]
print(f"Input: intervals = {intervals5}, newInterval = {newInterval5} -> Output: {solver.insert(intervals5, newInterval5)}") # Expected: [[0,6]]

# Приклад 6: Пустий масив
intervals6 = []
newInterval6 = [5,7]
print(f"Input: intervals = {intervals6}, newInterval = {newInterval6} -> Output: {solver.insert(intervals6, newInterval6)}") # Expected: [[5,7]]