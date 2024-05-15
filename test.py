from collections import deque

class Solution:
  def apply(self, generate_map):
    n = len(generate_map)
    q = deque([(0, 0)])
    generate_map[0][0] = 2
    ans = n * n - 1
    while q:
      x,y = q.popleft()
      for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and generate_map[nx][ny] == 0:
          generate_map[nx][ny] = 2
          ans -= 1
          q.append((nx, ny))
    return ans