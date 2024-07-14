# https://leetcode.cn/problems/minimum-cost-for-cutting-cake-ii/
from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        ans = i = j = 0
        cnt_h = cnt_v = 1
        while i < m - 1 or j < n - 1:
            if j == n - 1 or i < m - 1 and horizontalCut[i] > verticalCut[j]:
                ans += horizontalCut[i] * cnt_h  # 横切
                i += 1
                cnt_v += 1  # 需要竖切的蛋糕块增加
            else:
                ans += verticalCut[j] * cnt_v  # 竖切
                j += 1
                cnt_h += 1  # 需要横切的蛋糕块增加
        return ans