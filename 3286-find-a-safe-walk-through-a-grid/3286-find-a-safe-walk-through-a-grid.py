from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(0, 0, health - 1 if grid[0][0] == 1 else health)])
        visited = [[-1] * n for _ in range(m)]
        visited[0][0] = health

        while queue:
            x, y, current_health = queue.popleft()
            if x == m - 1 and y == n - 1 and current_health >= 1:
                return True

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n:
                    new_health = current_health - grid[new_x][new_y]
                    if new_health >= 1 and new_health > visited[new_x][new_y]:
                        visited[new_x][new_y] = new_health
                        queue.append((new_x, new_y, new_health))

        return False