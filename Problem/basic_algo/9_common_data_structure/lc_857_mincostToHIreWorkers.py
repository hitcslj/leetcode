# https://leetcode.cn/problems/minimum-cost-to-hire-k-workers
from typing import List 
from heapq import heapify,heapreplace

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        qw = sorted([p for p in zip(quality,wage)],key = lambda p:p[1]/p[0]) # 根据价/质比排序
        h = [-q for q,_ in qw[:k]] # 质量取负数
        heapify(h) # 质量最高的会放在堆顶部
        sum_q = -sum(h) # 先把该批质量求和
        r = qw[k-1][1]/qw[k-1][0] # 该批质量要按照最高的价/质比付钱
        ans = sum_q*r
        for q,w in qw[k:]:
            if q<-h[0]: # 只有当质量小的时候，才有可能出现更低的价值
                sum_q+=heapreplace(h,-q)+q # 质量的变化
                r = w/q # 新的价/质比
                ans = min(ans,sum_q*r)
        return ans
                