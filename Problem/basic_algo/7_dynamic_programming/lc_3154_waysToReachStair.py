# https://leetcode.cn/problems/find-number-of-ways-to-reach-the-k-th-stair
from functools import cache

class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dfs(i,j,preDown): # 当前位于台阶i, 已经使用了j次操作2，上一次是否使用操作1
            if i > k+1: # 永远回不来了
                return 0
            ans = 0
            if i == k:
                ans += 1
            ans += dfs(i+(1<<j), j+1, False) # 使用操作二
            if i and not preDown:
                ans += dfs(i-1,j,True) # 使用操作1
            return ans
        return dfs(1,0,False)