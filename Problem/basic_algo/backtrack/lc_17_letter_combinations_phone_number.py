# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
from typing import List

MAPPING = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n==0:
            return []
        res = []
        path = ['']*n
        def dfs(i:int) -> None:
            if i == n:
                res.append(''.join(path))
                return 
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i+1)
        dfs(0)
        return res
