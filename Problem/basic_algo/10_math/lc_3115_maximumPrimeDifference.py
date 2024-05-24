# 
from typing import List
from math import isqrt

# 枚举 100以内的质数
MX = 101
prime = [True]*MX
prime[0]=prime[1]=False
for i in range(2,isqrt(MX)+1):
    if not prime[i]:continue
    for j in range(i*i,MX,i):
        prime[j] = False

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        idx = []
        for i,num in enumerate(nums):
            if prime[num]:
                idx.append(i)
                break
        for i in range(len(nums)-1,-1,-1):
            if prime[nums[i]]:
                idx.append(i)
                break
        if len(idx)<2:
            return 0
        return idx[-1]-idx[0]
        
        
        
        