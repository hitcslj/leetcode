# https://leetcode.cn/problems/restore-ip-addresses/
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)>12:
            return []
        def dfs(i):
            if i==len(s):
                if len(path)==4:
                    res.append('.'.join(path))
                return 
            for j in range(i,min(i+3,len(s))):
                t = s[i:j+1]
                if check(t):
                    path.append(t)
                    dfs(j+1)
                    path.pop()

        def check(t):
            if len(t)>1 and t[0]=='0':return False
            if int(t)>255:return False
            return True
        
        res,path=[],[]
        dfs(0)
        return res