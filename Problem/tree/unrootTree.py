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


# https://leetcode.cn/problems/count-valid-paths-in-a-tree

from math import isqrt
MX = 10**5+1
isPrime = [True]*MX
isPrime[0] = isPrime[1] = False
for i in range(2,isqrt(MX)+1):
    if isPrime[i]:
        for j in range(i*i,MX,i):
            isPrime[j] = False

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n+1)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = 0
        def dfs(x,pa):
            nodes.append(x)
            for y in g[x]:
                if y!=pa and not isPrime[y]:
                    dfs(y,x)
        size = [0]*(n+1)
        # 枚举每个节点作为根节点的合法路径
        for i in range(1,n+1):
            if not isPrime[i]:continue
            cur = 0
            for x in g[i]:
                if isPrime[x]:continue
                if size[x]==0:
                    nodes = []
                    dfs(x,i)
                    for y in nodes:
                        size[y] = len(nodes)
                ans += cur * size[x]
                cur += size[x]
            ans += cur
        return ans


# https://leetcode.cn/problems/count-number-of-possible-root-nodes
    
class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges)+1
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        guesses = {(x,y) for x,y in guesses}
        ans = cnt0 = 0
        def dfs(x,pa):
            for y in g[x]:
                if y==pa:continue
                nonlocal cnt0
                cnt0 += (x,y) in guesses
                dfs(y,x)
        dfs(0,-1)
        def reroot(x,pa,cnt):
            nonlocal ans
            ans += cnt >= k #此时cnt就是以x为根的猜对次数
            for y in g[x]:
                if y==pa:continue
                reroot(y,x,cnt-((x,y) in guesses) + ((y,x) in guesses))

        reroot(0,-1,cnt0)
        return ans

        