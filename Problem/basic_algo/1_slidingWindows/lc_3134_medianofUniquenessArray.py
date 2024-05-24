from typing import List
from collections import Counter

# https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/
class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        left,right = 1,10**5
        total = n*(1+n)//2
        def check(x):
            total = 0
            cnt = Counter()
            left = 0
            for right,num in enumerate(nums):
                cnt[num]+=1
                while len(cnt)>x:
                    cnt[nums[left]] -= 1
                    if cnt[nums[left]] == 0:
                        del cnt[nums[left]]
                    left += 1
                total += right-left+1
            return total >= k
                
        k = (total+1)//2
        ans = left
        while left<=right:
            mid = (left+right)>>1
            if check(mid): # distant值<=mid, 不少于k个
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans