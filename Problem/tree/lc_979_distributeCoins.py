# https://leetcode.cn/problems/distribute-coins-in-binary-tree/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            if not root: return 0,0
            nodes_left,coins_left = dfs(root.left)
            nodes_right,coins_right = dfs(root.right)
            nonlocal ans
            ans += abs(nodes_left+nodes_right+1-(coins_left+coins_right+root.val))
            return nodes_left+nodes_right+1,coins_left+coins_right+root.val
        dfs(root)
        return ans
        