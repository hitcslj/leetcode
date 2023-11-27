# https://leetcode.cn/problems/sum-of-subarray-minimums/

from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stk = []
        left = [-1]*n
        right = [n]*n
        for i,v in enumerate(arr):
            while stk and arr[stk[-1]] > v:
                right[stk[-1]] = i
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        MOD = 10**9+7
        res = 0
        # print(left,right)
        for i,v in enumerate(arr):
            total = (i-left[i])*(right[i]-i)
            res = (res+v*total)%MOD
        return res
