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


# https://www.cnblogs.com/SEU-ZCY/p/14631735.html
class Solution:
    def findBuilding(self, heights: List[int]) -> List[int]:
        stack = []
        length = len(heights)
        res = [1] * length  # At least can see itself
        
        # Scan from right to left
        for i in range(length - 1, -1, -1):
            res[i] += len(stack)
            while stack and stack[-1] <= heights[i]:
                stack.pop()
            stack.append(heights[i])
        
        stack.clear()
        
        # Scan from left to right
        for i in range(length):
            res[i] += len(stack)
            while stack and stack[-1] <= heights[i]:
                stack.pop()
            stack.append(heights[i])
        
        return res

if __name__ == "__main__":
    arr = [5, 3, 8, 3, 2, 5]
    solution = Solution()
    res = solution.findBuilding(arr)
    print(res)
