# https://leetcode.cn/problems/partition-to-k-equal-sum-subsets
from typing import List
from functools import cache

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        
        if total%k!=0:return False
        target = total//k
        nums.sort() #方便后面减枝
        @cache
        def dfs(state,curSum):
            if state==(1<<n)-1:
                return True
            for i,num in enumerate(nums):
                if num+curSum>target: #大于的话，后面怎么也不可能等于了
                    break
                if (state>>i)&1==0 and dfs(state|(1<<i),(curSum+num)%target):
                    return True
            return False
        return dfs(0,0)