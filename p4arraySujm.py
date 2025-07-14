class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Крок 1: Сортуємо масив. Це дозволяє використовувати метод двох покажчиків.
        nums.sort()
        n = len(nums)

        # Ініціалізуємо closest_sum з сумою перших трьох елементів.
        # Це гарантує, що у нас є початкове значення для порівняння.
        closest_sum = nums[0] + nums[1] + nums[2]

        # Крок 2: Ітеруємо по масиву за допомогою одного покажчика (i)
        # та використовуємо метод двох покажчиків (left, right) для решти.
        # Ми йдемо до n-2, тому що нам потрібно щонайменше два елементи після nums[i].
        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Якщо поточна сума точно дорівнює target, це найкращий можливий результат.
                if current_sum == target:
                    return target

                # Перевіряємо, чи поточна сума ближча до target, ніж closest_sum.
                # Ми порівнюємо абсолютні різниці.
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Регулюємо покажчики left і right
                if current_sum < target:
                    # Сума занадто мала, збільшуємо лівий покажчик, щоб збільшити суму.
                    left += 1
                else:  # current_sum > target
                    # Сума занадто велика, зменшуємо правий покажчик, щоб зменшити суму.
                    right -= 1

        # Повертаємо суму, яка була найближчою до target.
        return closest_sum

# Приклади використання:
solver = Solution()

nums1 = [-1, 2, 1, -4]
target1 = 1
print(f"Input: nums = {nums1}, target = {target1} -> Output: {solver.threeSumClosest(nums1, target1)}") # Expected Output: 2

nums2 = [0, 0, 0]
target2 = 1
print(f"Input: nums = {nums2}, target = {target2} -> Output: {solver.threeSumClosest(nums2, target2)}") # Expected Output: 0

nums3 = [1, 1, 1, 0]
target3 = -100
print(f"Input: nums = {nums3}, target = {target3} -> Output: {solver.threeSumClosest(nums3, target3)}") # Expected Output: 2 (1+1+0) -> closest to -100 is 2

nums4 = [1, 2, 3, 4, 5]
target4 = 7
print(f"Input: nums = {nums4}, target = {target4} -> Output: {solver.threeSumClosest(nums4, target4)}") # Expected Output: 6 (1+2+3)