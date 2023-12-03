# 组合数学

# https://leetcode.cn/problems/count-the-number-of-infection-sequences
from typing import List
MOD = 10**9 + 7
MX = 10**5

# 组合数模板
fac = [0]*MX
fac[0] = 1
for i in range(1,MX):
    fac[i] = fac[i-1] * i % MOD

inv_fac = [0] * MX
inv_fac[MX-1] = pow(fac[MX-1],-1,MOD)
for i in range(MX-1,0,-1):
    inv_fac[i-1] = inv_fac[i] * i % MOD

def comb(n:int,k:int)->int:
    return fac[n] * inv_fac[k] % MOD * inv_fac[n-k] % MOD

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        sick.sort()
        m = len(sick)
        total = n-m # 剩余未被感染的数量
        ans = fac[total] * inv_fac[sick[0]] * inv_fac[n-1-sick[-1]] % MOD
        p = 0 
        for i in range(1,len(sick)):
            k = sick[i]-sick[i-1]-1
            if k:
                ans = ans * inv_fac[k] % MOD
                p += k-1
        return ans * pow(2,p,MOD) % MOD



