# https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/

from typing import List

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        cnt = [0]*n 

        # 暴力统计dfs
        def dfs1(x,pa,t):
            if x==t:
                cnt[x]+=1
                return True
            for y in g[x]:
                if y!=pa and dfs1(y,x,t):
                    cnt[x]+=1
                    return True
            return False

        for start,end in trips:
            dfs1(start,-1,end)
        
        # 类似打家劫舍
        def dfs(x, pa):
            not_halve = price[x] * cnt[x]
            halve = not_halve // 2
            for y in g[x]:
                if y!=pa:
                    nh,h = dfs(y,x)
                    not_halve += min(nh,h)
                    halve += nh
            return not_halve,halve
        return min(dfs(0,-1))

