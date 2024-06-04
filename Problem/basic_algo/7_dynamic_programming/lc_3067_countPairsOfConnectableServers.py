# https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network
from typing import List

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges)+1
        g = [[] for _ in range(n)]
        for a,b,w in edges:
            g[a].append((b,w))
            g[b].append((a,w))
        cnt = [0]*n
        def dfs(x,pa,curSum):
            cur = int(curSum % signalSpeed == 0)
            for y,w in g[x]:
                if y==pa:continue
                cur += dfs(y,x,curSum+w)
            return cur
        # 考虑以每个点为根节点
        for x in range(n):
            s = 0
            for y,w in g[x]:
                child = dfs(y,x,w)
                cnt[x] += s * child
                s += child
        return cnt