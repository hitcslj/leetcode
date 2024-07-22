from typing import List
from itertools import accumulate, pairwise

# https://leetcode.cn/problems/minimum-array-changes-to-make-differences-equal
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = [0] * (k + 2)
        for i in range(n // 2):
            p, q = nums[i], nums[n - 1 - i]
            if p > q:  # 保证 p <= q
                p, q = q, p
            x = q - p
            mx = max(q, k - p)
            # [0, x-1] 全部 +1：把 q-p 改成小于 x 的，只需要改 p 或 q 中的一个数
            d[0] += 1
            d[x] -= 1
            # [x+1, mx] 全部 +1：把 q-p 改成大于 x 小于等于 mx 的，也只需要改 p 或 q 中的一个数
            d[x + 1] += 1
            d[mx + 1] -= 1
            # [mx+1, k] 全部 +2：把 q-p 改成大于 mx 的，p 和 q 都需要改
            d[mx + 1] += 2
        return min(accumulate(d))
    
# https://leetcode.cn/problems/minimum-operations-to-make-array-equal-to-target
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        a = [0] + [t - x for x, t in zip(nums, target)] + [0]  # 前后加 0，方便计算
        return sum(max(y - x, 0) for x, y in pairwise(a))
    
# https://leetcode.cn/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        target = [0]+target
        return sum(max(b-a,0) for a,b in pairwise(target))
 
 