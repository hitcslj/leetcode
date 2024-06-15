# Source: https://leetcode.com/problems/burst-balloons/
from functools import cache

class  Solution:
  def maxCoins(self,nums):
    nums = nums + [1]
    @cache
    def dfs(l,r):
      if l > r:
        return 0
      return max(nums[l-1]*nums[i]*nums[r+1] + dfs(l,i-1) + dfs(i+1,r) for i in range(l+1,r))
    return dfs(0,len(nums)-2)

  