from typing import List
from math import lcm

# 一般化容斥远离+二分答案
# https://leetcode.cn/problems/kth-smallest-amount-with-single-denomination-combination/
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def check(m: int) -> bool:
            cnt = 0
            for i in range(1, 1 << len(coins)):  # 枚举所有非空子集
                lcm_res = 1  # 计算子集 LCM
                for j, x in enumerate(coins):
                    if i >> j & 1:
                        lcm_res = lcm(lcm_res, x)
                        if lcm_res > m:  # 太大了
                            break
                else:  # 中途没有 break
                    cnt += m // lcm_res if i.bit_count() % 2 else -(m // lcm_res)
            return cnt >= k
        
        left,right = k,min(coins)*k
        ans = k
        while left<=right:
            mid = (left+right)>>1
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans