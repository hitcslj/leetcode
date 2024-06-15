from typing import List
import math

# https://leetcode.cn/problems/gray-code/
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:return [0,1]
        pre = self.grayCode(n-1)
        back = []
        for num in pre[::-1]:
            back.append((1<<(n-1))+num)
        return pre + back

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i
        return ans

 
def gray_encode(bytenum): # 1111 -> 1000
    return bytenum^(bytenum>>1)


def gray_decode(gray): # 1000 -> 1111
        if not gray:return 0
        head = 1<<int(math.log2(gray))
        return head + gray_decode((gray^head)^(head>>1))

 