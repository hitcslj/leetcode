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

# https://leetcode.cn/problems/count-complete-substrings
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def f(s: str) -> int:
            ans = 0
            for l in range(1,27):
                window_size = l*k
                if window_size>len(s):
                    break
                freq = Counter(s[:window_size]) 
                cc = Counter(freq.values())
                if cc[k]==l:
                    ans += 1
                for in_,out in zip(s[window_size:],s):
                    cc[freq[in_]]-=1
                    freq[in_]+=1
                    cc[freq[in_]]+=1
                    cc[freq[out]]-=1
                    freq[out]-=1
                    cc[freq[out]]+=1
                    if cc[k]==l:
                        ans += 1
            return ans
        n = len(word)
        ans = i = 0
        while i<n:
            start = i
            i += 1
            while i<n and abs(ord(word[i])-ord(word[i-1]))<=2:
                i += 1
            ans += f(word[start:i])
        return ans

# https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-continuous
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        arr = sorted(set(nums))
        left = ans = 0
        for right,num in enumerate(arr):
            while arr[left]<num-n+1:
                left += 1
            ans = max(ans,right-left+1)
        return n - ans