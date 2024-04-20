# https://leetcode.cn/problems/palindrome-partitioning/
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i):
            if i==len(s):
                res.append(path[:])
                return 
            for j in range(i,len(s)):
                if isPalindrome(s,i,j):
                    path.append(s[i:j+1])
                else:
                    continue
                dfs(j+1)
                path.pop()

        def isPalindrome(s,start,end):
            while start<=end:
                if s[start]!=s[end]:return False
                start+=1
                end-=1
            return True
        
        res,path=[],[]
        dfs(0)
        return res