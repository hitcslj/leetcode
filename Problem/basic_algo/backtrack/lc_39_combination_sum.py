# https://leetcode.cn/problems/combination-sum
from typing import List



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def dfs(i,curSum):
            if curSum > target or i == len(candidates):
                return 
            if curSum == target:
                res.append(path[:])
                return
            # 不选 
            dfs(i+1,curSum)

            # 选
            path.append(candidates[i])
            dfs(i,curSum+candidates[i])
            path.pop()
        dfs(0,0)
        return res

        

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def dfs(i,curSum):
            if curSum == target:
                res.append(path[:])
                return 
            # 选哪个数
            for j in range(i,len(candidates)):
                if curSum + candidates[j] > target: return
                path.append(candidates[j])
                dfs(j,curSum+candidates[j])
                path.pop()
        dfs(0,0)
        return res