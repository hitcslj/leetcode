from typing import List, Optional
from math import inf
from functools import cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.cn/problems/house-robber-iii/
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:return [0,0]
            left = dfs(root.left)
            right = dfs(root.right)
            ans = [0,0]
            ans[0] = left[1]+right[1]+root.val
            ans[1] = max(left)+max(right)
            return ans # [偷，不偷]
        return max(dfs(root))

# https://leetcode.cn/problems/find-the-maximum-sum-of-node-values
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(x,pa): # 不操作 pa-x， 操作 pa-x 
            f0, f1 = 0, -inf
            for y in g[x]:
                if y != pa:
                    r0, r1 = dfs(y, x)
                    f0, f1 = max(f0 + r0, f1 + r1), max(f1 + r0, f0 + r1)
            return max(f0 + nums[x], f1 + (nums[x] ^ k)), max(f1 + nums[x], f0 + (nums[x] ^ k))
        return dfs(0,-1)[0]

# https://leetcode.cn/problems/choose-edges-to-maximize-score-in-a-tree/
class Solution:
    def maxScore(self, edges: List[List[int]]) -> int:
        n = len(edges)+1
        g = [dict() for _ in range(n)]
        for i,(pa,wt) in enumerate(edges):
            if pa==-1:continue
            g[i][pa] = wt
            g[pa][i] = wt
        @cache
        def dfs(x,pa): # 不操作pa-x, 操作pa-x
            s = 0
            for y in g[x].keys():
                if y!=pa:
                    s += dfs(y,x)[0] # x-y均不操作求和
            f0 = s  
            f1 = s+g[x][pa] if pa!=-1 else -inf
            for y in g[x].keys():
                if y!=pa:
                    r0,r1 = dfs(y,x)
                    f0 = max(f0,s-r0+r1) # 可以选择一个x-y
            return f0,f1
        return dfs(0,-1)[0]


# https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/
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

# https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges)+1
        g = [[] for _ in range(n)]
        for a,b,w in edges:
            g[a].append((b,w))
            g[b].append((a,w))
            
        
        def dfs(x,pa,curSum):
            cur = int(curSum % signalSpeed == 0)
            for y,w in g[x]:
                if y!=pa:cur += dfs(y,x,curSum+w)
            return cur
        
        # 考虑以每个点为根节点
        cnt = [0]*n
        for x in range(n):
            s = 0
            for y,w in g[x]:
                child = dfs(y,x,w)
                cnt[x] += s * child
                s += child
        return cnt

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

        