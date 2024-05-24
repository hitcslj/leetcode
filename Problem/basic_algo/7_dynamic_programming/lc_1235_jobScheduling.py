# https://leetcode.cn/problems/maximum-profit-in-job-scheduling
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        offers = sorted(zip(startTime,endTime,profit),key=lambda x:x[1])
        preEnd = []
        f = [-1]*n # f[i]表示选择了第i份工作后，之前还可以选择的工作最晚时间编号
        for i in range(1,n):
            preEnd.append(offers[i-1][1])
            j = bisect_right(preEnd,offers[i][0])
            f[i] = j-1
        
        @cache
        def dfs(i):
            if i<0:return 0
            # 不选 & 选
            return max(dfs(i-1),dfs(f[i])+offers[i][2])
        return dfs(n-1)

