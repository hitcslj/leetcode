# https://leetcode.cn/problems/strobogrammatic-number-ii/
from typing import List
from functools import cache

class Solution:
    @cache
    def findStrobogrammatic(self, n: int) -> List[str]:
        if not n:
            return ['']
        elif n == 1:
            return ['0', '1', '8']
        res = set()
        for ans in self.findStrobogrammatic(n-2):
            if n > 3:
                res.add('10'+ ans[1:-1] + '01')
                res.add('60' + ans[1:-1] + '09')
                res.add('80' + ans[1:-1] + '08')
                res.add('90' + ans[1:-1] + '06')
            res.add('1' + ans + '1')
            res.add('6' + ans + '9')
            res.add('8' + ans + '8')
            res.add('9' + ans + '6')
        return list(res)

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        mpt = {
            '0':'0',
            '1':'1',
            '6':'9',
            '8':'8',
            '9':'6'
        }
        
        def f(s):
            ans = ['']*n
            if n%2==0:
                for i in range(len(s)):
                    ans[i] = s[i]
                    ans[-i-1] = mpt[s[i]]
            else:
                ans[len(s)-1]=s[-1]
                for i in range(len(s)-1):
                    ans[i] = s[i]
                    ans[-i-1] = mpt[s[i]]
            return ''.join(ans)

        def dfs(i): #  
            if i == n//2 + int(n%2==1):
                res.append(f(''.join(path)))
                return 
            if i == n//2 :
                for d in '018':
                    path[i] = d
                    dfs(i+1)
            elif i == 0:
                for d in '1689':
                    path[i] = d
                    dfs(i+1)
            else:
                for d in '01689':
                    path[i] = d
                    dfs(i+1)
        res = []
        path = ['']*(n//2 + int(n%2==1))
        dfs(0)
        return res
        

