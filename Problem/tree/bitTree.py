# https://leetcode.cn/problems/range-sum-query-mutable

from typing import List

class BinaryIndexedTree:
    __slots__ = ["n", "c"]

    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, delta: int):
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s


class NumArray:
    __slots__ = ["tree"]

    def __init__(self, nums: List[int]):
        self.tree = BinaryIndexedTree(len(nums))
        for i, v in enumerate(nums, 1):
            self.tree.update(i, v)

    def update(self, index: int, val: int) -> None:
        prev = self.sumRange(index, index)
        self.tree.update(index + 1, val - prev)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(right + 1) - self.tree.query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


# https://leetcode.cn/problems/maximum-sum-queries/
from bisect import bisect_left

class BinaryIndexedTree:
    __slots__ = ["n", "c"]

    def __init__(self, n: int):
        self.n = n
        self.c = [-1] * (n + 1)

    def update(self, x: int, v: int):
        while x <= self.n:
            self.c[x] = max(self.c[x], v)
            x += x & -x

    def query(self, x: int) -> int:
        mx = -1
        while x:
            mx = max(mx, self.c[x])
            x -= x & -x
        return mx


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        nums = sorted(zip(nums1,nums2),key=lambda x:-x[0])
        nums2.sort()
        n,m = len(nums1),len(queries)
        ans = [-1]*m
        j = 0
        tree = BinaryIndexedTree(n)
        for i in sorted(range(m),key=lambda i:-queries[i][0]):
            x,y = queries[i]
            while j<n and nums[j][0]>=x:
                k = n - bisect_left(nums2,nums[j][1])
                tree.update(k,nums[j][0]+nums[j][1])
                j += 1
            k = n - bisect_left(nums2,y)
            ans[i] = tree.query(k)
        return ans
