# https://leetcode.cn/problems/special-permutations
from typing import List
from functools import cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        u = (1<<n) - 1
        mod = 10**9 + 7
        @cache 
        def dfs(state, cur): # 当前可选集合用state来记录，选的数字为cur
            if state == 0:
                return 1
            res = 0
            for i in range(n):
                if state>>i & 1 and (nums[i]%cur==0 or cur%nums[i]==0):
                    res = (res + dfs(state ^(1<<i),nums[i]))%mod
            return res    
        return sum(dfs(u^(1<<i),nums[i]) for i in range(n)) % mod