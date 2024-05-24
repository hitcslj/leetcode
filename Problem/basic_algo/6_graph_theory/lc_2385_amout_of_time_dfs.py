# https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected
from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = defaultdict(list)
        def dfs(node,pa):
            if not node: return 
            if pa:
                g[node.val].append(pa.val)
                g[pa.val].append(node.val)
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root, None) # build the graph

        def dfs2(node, pa):
            ans = 0
            for nxt in g[node]:
                if nxt != pa:
                    ans = max(ans, dfs2(nxt,node)+1)
            return ans
        return dfs2(start,-1) # return the max depth of the tree （root is start）