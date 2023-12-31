# https://leetcode.cn/problems/longest-duplicate-substring/description/

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # 字符串哈希
        n = len(s)
        base, mod = 1331, 10**20 + 7
        nums = [ord(c)-ord('a') for c in s]

        def check(m): # 字符串中出现长度为m的重复子字符串
            seen = set()
            # 先对[0,m-1]编码
            h = 0
            base_m = pow(base,m,mod)
            for i in range(m):
                h = (h*base+nums[i])%mod
            seen.add(h)
            for i in range(1,n-m+1):
                h = (h*base-nums[i-1]*base_m+nums[i+m-1])%mod
                if h in seen:
                    return i
                seen.add(h)
            return -1


        
        left,right = 1,n-1
        start,l = -1,0
        while left<=right:
            mid = (left+right)>>1
            idx = check(mid)
            if idx!=-1:
                start = idx
                l = mid
                left = mid + 1
            else:
                right = mid - 1
        return s[start:start+l] if start!=-1 else ''