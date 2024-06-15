# https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work
from typing import List

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        m = max(milestones)
        s = sum(milestones)
        if m>s-m:
            return (s-m)*2 + 1
        else:
            # if s&1:
            #     return s-1
            # else:
            return s