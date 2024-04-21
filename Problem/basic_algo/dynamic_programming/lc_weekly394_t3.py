# https://leetcode.cn/problems/minimum-number-of-operations-to-satisfy-conditions/

from typing import List
from functools import cache

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        # 可以先统计每一列的数字，然后采用dp的方式
        cnt = [[0]*10 for _ in range(n)]
        for row in grid:
            for j,x in enumerate(row):
                cnt[j][x] += 1
        
        @cache
        def dfs(j,pre):
            if j==n:return 0
            return min(m - cnt[j][num]+dfs(j+1,num) for num in range(10) if num != pre)
        return dfs(0,-1)