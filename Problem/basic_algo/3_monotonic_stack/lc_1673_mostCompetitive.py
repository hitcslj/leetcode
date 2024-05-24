# https://leetcode.cn/problems/find-the-most-competitive-subsequence
from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stk = []
        for i in range(n):
            while stk and stk[-1]>nums[i] and len(stk) + n -i > k:
                stk.pop()
            if len(stk)<k:
                stk.append(nums[i])
        return stk 
