from typing import List
from math import inf

# https://leetcode.cn/problems/paint-house-ii/
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n,k = len(costs),len(costs[0])
        dp = costs[0]
        first, second = inf, inf
        for v in dp:
            if v<first:
                first,second = v,first
            elif v<second:
                second = v
        for i in range(1,n):
            dpNew = [0]*k
            firstNew,secondNew = inf,inf
            for j,c in enumerate(costs[i]):
                prevMin = second if dp[j]==first else first # 不能相邻
                dpNew[j] = prevMin+c
                if dpNew[j]<firstNew:
                    firstNew,secondNew = dpNew[j],firstNew
                elif dpNew[j]<secondNew:
                    secondNew = dpNew[j]
            dp,first,second = dpNew,firstNew,secondNew
        return min(dp)