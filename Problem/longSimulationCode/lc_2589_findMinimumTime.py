# https://leetcode.cn/problems/minimum-time-to-complete-all-tasks
from typing import List

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1])
        run = [False]*2001 # 暴力枚举每个时间是否运行
        for start,end,d in tasks:
            d -= sum(run[start:end+1])
            if d<=0:continue
            for i in range(end,start-1,-1): # 贪心，从后往前
                if run[i]:continue
                run[i] = True
                d -= 1
                if d<=0:break
        return sum(run)