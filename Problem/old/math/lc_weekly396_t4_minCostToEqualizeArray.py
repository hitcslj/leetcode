# https://leetcode.cn/problems/minimum-cost-to-equalize-array
from typing import List

class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        n = len(nums)
        s = n*max(nums) - sum(nums)
        mx = max(nums)-min(nums)
        mod = 10**9+7
        
        if max(nums) == min(nums): return 0
        def check(s,m):
            if m > s-m:
                return (s-m)*cost2 + (2*m-s)*cost1
            else:
                if s&1:
                    return s//2 * cost2 + cost1
                else:
                    return s//2 * cost2
        
        if 2*cost1 <= cost2:
            # 采用操作1
            return s*cost1 % mod
        else:
            return min(check(s+n*i,mx+i) for i in range(mx+1))%mod
            
            
                
            
            