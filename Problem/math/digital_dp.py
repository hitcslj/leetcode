# https://leetcode.cn/problems/count-the-number-of-powerful-integers/solutions/2595149/shu-wei-dp-shang-xia-jie-mo-ban-fu-ti-da-h6ci/

from typing import List
from functools import cache



# https://leetcode.cn/problems/count-the-number-of-powerful-integers
# low-high 一次记忆化dfs完成
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        low = str(start)
        high = str(finish)
        n = len(high)
        low = '0'*(n-len(low)) + low
        diff = n - len(s)

        @cache
        def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1
            
            # 第 i 个数位可以从 lo 枚举到 hi
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9

            res = 0
            if i < diff:
                for d in range(lo, min(hi,limit)+1):
                    res += dfs(i+1, limit_low and d==lo, limit_high and d==high)
            else:
                x = int(s[i - diff])
                if lo <= x <= min(hi,limit):
                    res = dfs(i+1,limit_low and x==lo, limit_high and x==hi)
            return res
        return dfs(0,True,True)

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        high = str(finish)
        low = str(start-1)
        n = len(high)
        low = '0'*(n-len(low)) + low
        diff = n - len(s)
        def cal(t):
            if int(t)<int(s):return 0
            @cache
            def dfs(i: int, limit_high: bool) -> int:
                if i == n:
                    return 1
                res = 0
                hi = int(t[i]) if limit_high else 9
                if i < diff:
                    for d in range(min(hi,limit)+1):
                        res += dfs(i+1,limit_high and d==hi)
                else:
                    x = int(s[i - diff])
                    if x <= min(hi,limit):
                        res = dfs(i+1,limit_high and x==hi)
                return res
            return  dfs(0,True)
        return cal(high) - cal(low)


# https://leetcode.cn/problems/number-of-beautiful-integers-in-the-range
# 类似前缀和，计算两次
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def cal(s:str):
            @cache
            def f(s:str,i:int,is_num:bool,is_limit:bool,cnt:int,val:int):
                if i==len(s):
                    return is_num and cnt==0 and val==0
                res = 0
                if not is_num:
                    res = f(s,i+1,False,False,cnt,val)
                up = int(s[i]) if is_limit else 9
                for d in range(1-int(is_num),up+1):
                    res += f(s,i+1,True,is_limit and d==up,cnt + (1 if d%2 else -1), (10*val+d) % k)
                return res
            return f(s,0,False,True,0,0)
        
        return cal(str(high))-cal(str(low-1))