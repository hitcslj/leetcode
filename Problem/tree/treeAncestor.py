from typing import List
from math import gcd

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.p = [[-1]*18 for _ in range(n)] # self.p[i][j], 节点i往上走2^j个节点
        for i,pa in enumerate(parent):
            self.p[i][0] = pa
        for j in range(1,18): # 往上2^j个节点 
            for i in range(n):
                if self.p[i][j-1] == -1:
                    continue
                mid = self.p[i][j-1] # i往上走2^{j-1}步
                self.p[i][j] = self.p[mid][j-1] # mid继续往上走2^{j-1}步



    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(17,-1,-1):
            if k>>i & 1:
                node = self.p[node][i]
                if node == -1:
                    break
        return node




# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
    


# https://leetcode.cn/problems/tree-of-coprimes
# 预处理：coprime[i] 保存 [1, MX) 中与 i 互质的所有元素
MX = 51
coprime = [[j for j in range(1, MX) if gcd(i, j) == 1]
           for i in range(MX)]
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        g = [[] for _ in range(n)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        g[0].append(-1) # 根节点
        mpt = [(-1,-1)]*MX
        ans = [-1]*n
        def dfs(x,pa,depth): # mpt保存父节点的值和最新的节点
            val = nums[x]  # x 的节点值
            ans[x] = max(mpt[j] for j in coprime[val])[1]
            tmp = mpt[nums[x]]
            mpt[nums[x]] = (depth,x)
            for y in g[x]:
                if y != pa:
                    dfs(y,x,depth+1)
            mpt[nums[x]] = tmp
        dfs(0,-1,0)
        return ans

                


