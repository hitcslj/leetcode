# https://leetcode.cn/problems/maximum-strong-pair-xor-ii/

from typing import List
from collections import deque

class TrieBit:
    def __init__(self, n=20):
        """template of add and remove num for maximum xor query"""
        self.dct = dict()
        self.n = n
        return

    def update(self, num):
        cur = self.dct
        for i in range(self.n, -1, -1):
            w = 1 if num & (1 << i) else 0
            if w not in cur:
                cur[w] = dict()
            cur = cur[w]
            cur["cnt"] = cur.get("cnt", 0) + 1
        return

    def query(self, num):
        """query maximum xor value"""
        cur = self.dct
        ans = 0
        for i in range(self.n, -1, -1):
            w = 1 if num & (1 << i) else 0
            if 1 - w in cur:
                cur = cur[1 - w]
                ans |= 1 << i
            else:
                cur = cur[w]
        return ans

    def delete(self, num):
        """remove one num"""
        cur = self.dct
        for i in range(self.n, -1, -1):
            w = 1 if num & (1 << i) else 0
            if cur[w].get("cnt", 0) == 1:
                del cur[w]
                break
            cur = cur[w]
            cur["cnt"] -= 1
        return

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        trie = TrieBit()
        nums = sorted(set(nums))
        ans = 0
        q = deque()
        for y in nums:
            while q and q[0]*2<y:
                x = q.popleft()
                trie.delete(x)
            trie.update(y)
            q.append(y)
            ans = max(ans,trie.query(y))
        return ans