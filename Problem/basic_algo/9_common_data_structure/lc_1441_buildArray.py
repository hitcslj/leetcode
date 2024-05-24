# https://leetcode.cn/problems/build-an-array-with-stack-operations/
from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        j = 0
        ans = []
        for i in range(1,n+1):
            ans.append('Push')
            if  i != target[j]:
                ans.append('Pop')
            else:
                j += 1
            if j == len(target):
                break
        return ans