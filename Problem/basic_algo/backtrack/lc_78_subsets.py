# https://leetcode.cn/problems/subsets/description/
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(i: int) -> None:
            if i==len(nums):
                res.append(path.copy())
                return
            # 不选nums[i]
            dfs(i+1)
            # 选nums[i]
            path.append(nums[i])
            dfs(i+1)
            path.pop() # 恢复现场
        dfs(0)  
        return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(i: int) -> None:
            res.append(path.copy())
            for j in range(i,len(nums)):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)  
        return res