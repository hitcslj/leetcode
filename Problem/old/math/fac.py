# https://leetcode.cn/problems/minimum-factorization
class Solution:
    def smallestFactorization(self, num: int) -> int:
        res = []
        for i in range(9, 1, -1):
            while num % i == 0:
                res.append(i)
                num //= i
        if num > 9:
            return 0
        res = res[::-1]
        ans = 0
        for i in res:
            ans = ans * 10 + i
        if ans > 2 ** 31 - 1:
            return 0
        return ans