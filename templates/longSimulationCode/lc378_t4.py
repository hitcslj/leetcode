from typing import List
from collections import Counter
from itertools import accumulate

# https://leetcode.cn/problems/palindrome-rearrangement-queries/description/

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # 分成左右两半，右半反转
        n = len(s) // 2
        t = s[n:][::-1]
        s = s[:n]
        if s==t:
            return [True]*len(queries)
        if Counter(s)!=Counter(t):
            return [False]*len(queries)
        # 预处理三种前缀和
        def preSum(s):
            cnt = [[0] * 26 for _ in range(n + 1)]
            for i, c in enumerate(s):
                cnt[i + 1] = cnt[i][:]
                cnt[i + 1][ord(c) - ord('a')] += 1
            return cnt
        sum_s = preSum(s)
        sum_t = preSum(t)
        sum_ne = list(accumulate((x != y for x, y in zip(s, t)), initial=0))

        # 计算子串中各个字符的出现次数，闭区间 [l,r]
        def count(sum: List[List[int]], l: int, r: int) -> List[int]:
            return [x - y for x, y in zip(sum[r + 1], sum[l])]

        def subtract(s1: List[int], s2: List[int]) -> List[int]:
            for i, s in enumerate(s2):
                s1[i] -= s
                if s1[i] < 0:
                    return False
            return s1

        def check(l1: int, r1: int, l2: int, r2: int, sumS: List[List[int]], sumT: List[List[int]]) -> bool:
            # [0,l1-1] 有 s[i] != t[i] 或者 [max(r1,r2)+1,n-1] 有 s[i] != t[i]
            if sum_ne[l1] > 0 or sum_ne[n] - sum_ne[max(r1, r2) + 1] > 0:
                return False
            if r2 <= r1:  # 区间包含
                return count(sumS, l1, r1) == count(sumT, l1, r1)
            if r1 < l2:  # 区间不相交
                # [r1+1,l2-1] 都满足 s[i] == t[i]
                return sum_ne[l2] - sum_ne[r1 + 1] == 0 and \
                    count(sumS, l1, r1) == count(sumT, l1, r1) and \
                    count(sumS, l2, r2) == count(sumT, l2, r2)
            # 区间相交但不包含
            s1 = subtract(count(sumS, l1, r1), count(sumT, l1, l2 - 1))
            s2 = subtract(count(sumT, l2, r2), count(sumS, r1 + 1, r2))
            return s1 and s2 and s1 == s2

        ans = [False] * len(queries)
        for i, (l1, r1, c, d) in enumerate(queries):
            l2, r2 = n * 2 - 1 - d, n * 2 - 1 - c
            ans[i] = check(l1, r1, l2, r2, sum_s, sum_t) if l1 <= l2 else \
                     check(l2, r2, l1, r1, sum_t, sum_s)
        return ans