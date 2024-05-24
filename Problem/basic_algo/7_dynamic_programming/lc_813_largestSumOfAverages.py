# https://leetcode.cn/problems/largest-sum-of-averages/
from typing import List
from functools import cache

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        mean = [[0]*n for _ in range(n)]
        for l in range(n):
            cnt = 0
            for r in range(l,n):
                cnt += nums[r]
                mean[l][r] = cnt/(r-l+1)
        @cache
        def dfs(i,j): # 划分剩余i次，范围为0...j
            if i==0:
                return mean[0][j]
            return max(dfs(i-1,L-1)+mean[L][j] for L in range(i,j+1))
        return dfs(k-1,n-1)