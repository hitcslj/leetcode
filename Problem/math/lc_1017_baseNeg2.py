# https://leetcode.cn/problems/convert-to-base-2
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0: return '0'
        if n == 1: return '1'
        return self.baseNeg2((n-1)//-2) + '1' if n & 1 else self.baseNeg2(n//-2) + '0'
      