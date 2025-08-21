class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def depth_firdt_search(i, j):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            # base case
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            down_paths = depth_firdt_search(i + 1, j)
            right_paths = depth_firdt_search(i, j + 1)

            memo[(i, j)] = down_paths + right_paths
            return memo[(i, j)]

        return depth_firdt_search(0, 0)

# Приклад 1: З перешкодою
obstacleGrid1 = [[0,0,0],[0,1,0],[0,0,0]]
print(f"Input: {obstacleGrid1} -> Output: {Solution().uniquePathsWithObstacles(obstacleGrid1)}") # Очікуваний результат: 2

# Приклад 2: З перешкодою
obstacleGrid2 = [[0,1],[0,0]]
print(f"Input: {obstacleGrid2} -> Output: {Solution().uniquePathsWithObstacles(obstacleGrid2)}") # Очікуваний результат: 1

# Приклад 3: Початкова комірка - перешкода
obstacleGrid3 = [[1,0],[0,0]]
print(f"Input: {obstacleGrid3} -> Output: {Solution().uniquePathsWithObstacles(obstacleGrid3)}") # Очікуваний результат: 0

# Приклад 4: Без перешкод (як у Unique Paths I)
obstacleGrid4 = [[0,0],[0,0]]
print(f"Input: {obstacleGrid4} -> Output: {Solution().uniquePathsWithObstacles(obstacleGrid4)}") # Очікуваний результат: 2