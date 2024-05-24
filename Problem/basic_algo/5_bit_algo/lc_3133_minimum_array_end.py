# https://leetcode.cn/problems/minimum-array-end/
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x # x为1的位置不能动，为0的位置往里面填，
        i = 0
        n -= 1 # 000,001,002， ..., bin(n-1) 共n个数字， 将bin(n-1)往x为0的空位填好即可
        while n:
            if (x>>i)&1==0:
                if n&1:ans |= (1<<i)
                n >>= 1
            i += 1
        return ans