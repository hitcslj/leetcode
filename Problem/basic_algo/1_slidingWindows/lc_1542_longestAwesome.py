# https://leetcode.cn/problems/find-longest-awesome-substring

class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        mpt = {0:-1}
        ans = 1
        mask = 0
        for i,d in enumerate(s):
            d = int(d)
            mask ^= (1<<d)
            if mask in mpt:
                ans = max(ans,i-mpt[mask])
            else:
                mpt[mask] = i
            for j in range(10):
                if mask ^ (1<<j) in mpt:
                    ans = max(ans,i-mpt[mask ^ (1<<j)])
        return ans