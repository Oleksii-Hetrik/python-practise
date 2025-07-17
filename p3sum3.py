class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Крок 1: Сортуємо масив.
        nums.sort()
        n = len(nums)
        result = []  # Список для зберігання унікальних трійок

        # Крок 2: Ітеруємо по масиву за допомогою одного покажчика (i)
        # та використовуємо метод двох покажчиків (left, right) для решти.
        # Ми йдемо до n-2, тому що нам потрібно щонайменше два елементи після nums[i].
        for i in range(n - 2):
            # Обробка дублікатів для nums[i]
            # Якщо поточний елемент такий же, як попередній, ми пропускаємо його,
            # щоб уникнути дублікатів у наборі рішень.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Визначаємо target_sum для двох інших елементів
            target_sum_for_two = -nums[i]

            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target_sum_for_two:
                    # Знайшли трійку, яка сумується до 0
                    result.append([nums[i], nums[left], nums[right]])

                    # Обробка дублікатів для nums[left] та nums[right]
                    # Збільшуємо left, поки він не вказує на унікальний елемент
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Зменшуємо right, поки він не вказує на унікальний елемент
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Переходимо до наступних унікальних елементів
                    left += 1
                    right -= 1
                elif current_sum < target_sum_for_two:
                    # Сума занадто мала, збільшуємо лівий покажчик
                    left += 1
                else:  # current_sum > target_sum_for_two
                    # Сума занадто велика, зменшуємо правий покажчик
                    right -= 1

        return result

# Приклади використання:
solver = Solution()

nums1 = [-1, 0, 1, 2, -1, -4]
print(f"Input: nums = {nums1} -> Output: {solver.threeSum(nums1)}") # Expected Output: [[-1,-1,2],[-1,0,1]] (order might vary)

nums2 = [0, 1, 1]
print(f"Input: nums = {nums2} -> Output: {solver.threeSum(nums2)}") # Expected Output: []

nums3 = [0, 0, 0]
print(f"Input: nums = {nums3} -> Output: {solver.threeSum(nums3)}") # Expected Output: [[0,0,0]]

nums4 = [-2, 0, 1, 1, 2]
print(f"Input: nums = {nums4} -> Output: {solver.threeSum(nums4)}") # Expected Output: [[-2,0,2],[-2,1,1]]

nums5 = [1, -1, -1, 0]
print(f"Input: nums = {nums5} -> Output: {solver.threeSum(nums5)}") # Expected Output: [[-1,0,1]]

nums5 = [1, -1, -1, 0]
print(f"Input: nums = {nums5} -> Output: {solver.threeSum(nums5)}") # Expected Output: [[-1,0,1]]