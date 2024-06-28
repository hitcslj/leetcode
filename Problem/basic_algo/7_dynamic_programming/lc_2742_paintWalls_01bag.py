# https://leetcode.cn/problems/painting-the-walls
from typing import List
from functools import cache
from math import inf

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        @cache
        def dfs(i,c):  
            if c <= 0: return 0
            if i<0:return inf
            # 付费物体时间 >= 免费物体个数
            # 付费物体时间 >= n - 付费物体个数
            # c1 + ... + cj + j >= n
            # (c1+1)+ ... + (cj+1) >=n
            return min(dfs(i-1,c-time[i]-1)+cost[i],dfs(i-1,c))
        
        # 0-1背包问题，物体价值为cost[i],物体体积为time[i]+1, 选的体积超过n的，价值最小
        return dfs(n-1,n)