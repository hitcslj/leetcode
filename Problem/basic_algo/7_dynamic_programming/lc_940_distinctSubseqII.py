# https://leetcode.cn/problems/distinct-subsequences-ii/
from functools import cache

# classic subseq 统计问题
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(i,c): # s[0...i]中以c结尾的子序列个数
            if i == 0:
                return ord(s[i])-ord('a')==c
            if c == ord(s[i])-ord('a'): # 将之前的子序列都拼过来
                return sum(dfs(i-1,a) for a in range(26))+1 % MOD
            return dfs(i-1,c) 
        return sum(dfs(len(s)-1,a) for a in range(26))%MOD
