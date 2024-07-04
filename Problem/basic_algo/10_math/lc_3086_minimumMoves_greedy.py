# https://leetcode.cn/problems/minimum-moves-to-pick-k-ones
from typing import List
from functools import accumulate
from math import inf


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        pos = []
        c = 0 # nums中连续1的长度
        for i,x in enumerate(nums):
            if x == 0: continue
            pos.append(i)
            c = max(c,1)
            if i > 0 and nums[i-1]==1:
                if i > 1 and nums[i-2]==1:
                    c = 3
                else:
                    c = max(c,2)
        if k <= c:
            return k-1 # 第二种操作
        elif maxChanges+c>=k:
            return max(c-1,0) + 2*(k-c) # 除了连续c，其余k-c个1两次操作即可搞定
        else:
            n = len(pos)
            preSum = list(accumulate(pos,initial=0))
            ans = inf
            # 除了max_changes个数可以用两次操作得到，其余的1只能一步步移动到pos[i]
            size = k - maxChanges
            for right in range(size,n+1):
                # s1 + s2 是 j 在 [left,right) 中的所有pos[j] 到 pos[(left+right)/2]的距离之和
                left = right - size
                i = left + size // 2
                s1 = pos[i] * (i-left) - (preSum[i]-preSum[left])
                s2 = preSum[right] - preSum[i] - pos[i] * (right-i)
                ans = min(ans,s1 + s2)
            return ans + maxChanges*2

