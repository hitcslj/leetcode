# https://leetcode.cn/problems/count-beautiful-substrings-ii/

from typing import List
from collections import defaultdict,Counter

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        nums = []
        for c in s:
            if c in vowels:
                nums.append(1)
            else:
                nums.append(-1)
        cnt = defaultdict(list)
        cnt[0].append(-1)
        preSum = 0
        for i,num in enumerate(nums):
            preSum += num
            cnt[preSum].append(i)
        ## 同一个preSum的，任意两个索引之间的差距构成
        ans = 0
        k*=4
        def getSqrt(num):
            ## 将num进行质因数分解，质因数的幂数e
            divisor = 2
            ans = 1
            while num > 1:
                if num % divisor == 0:
                    count = 0
                    while num % divisor == 0:
                        num //= divisor
                        count += 1
                    ans *= divisor ** ((count+1)//2)
                divisor += 1
            return ans
            
            
        t = getSqrt(k)
        for arr in cnt.values():
            cur = [arr[i]-arr[i-1] for i in range(1,len(arr))]
            # cur子数组和
            cnt1 = Counter([0])
            r = 0
            for num in cur:
                r = (r+num)%t
                ans += cnt1[r]
                cnt1[r] += 1
        return ans