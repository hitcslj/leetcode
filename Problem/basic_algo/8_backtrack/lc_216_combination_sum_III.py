# https://leetcode.cn/problems/combination-sum-iii

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1,10))
        def dfs(i,curSum):
            if curSum == n and len(path)==k:
                res.append(path[:])
                return
            if i==len(nums) or curSum>n or len(path)>k:
                return
            for j in range(i,len(nums)):
                path.append(nums[j])
                dfs(j+1,curSum+nums[j])
                path.pop()
        res = []
        path = []
        dfs(0,0)
        return res