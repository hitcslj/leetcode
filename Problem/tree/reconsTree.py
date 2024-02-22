from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = {num:i for i,num in enumerate(postorder)}
        def dfs(preL,preR,posL,posR):
            if preL>preR or posL>posR:return None
            root = TreeNode(preorder[preL])
            if preL==preR:return root
            left_size = dic[preorder[preL+1]] - posL + 1 # 左子树的根节点在后序遍历中就是一个分界点
            root.left = dfs(preL+1,preL+left_size,posL,posL+left_size-1)
            root.right = dfs(preL+left_size+1,preR,posL+left_size,posR-1)
            return root
        return dfs(0,len(preorder)-1,0,len(postorder)-1) 

# preorder = [1,2,4,5,3,6,7]
# postorder = [4,5,2,6,7,3,1]
# ans = Solution().constructFromPrePost(preorder,postorder)
# print(ans)

# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = {num:i for i,num in enumerate(inorder)}
        def dfs(pl,pr,il,ir):
            if pl>pr:return None
            root = TreeNode(preorder[pl])
            mid = dic[root.val]
            left_size = dic[root.val] - il
            root.left = dfs(pl+1,pl+left_size,il,mid-1)
            root.right = dfs(pl+left_size+1,pr,mid+1,ir)
            return root
        return dfs(0,len(preorder)-1,0,len(inorder)-1)

# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = {num:i for i,num in enumerate(inorder)}
        def dfs(pl,pr,il,ir):
            if pl>pr:return None
            root = TreeNode(postorder[pr])
            mid = dic[root.val]
            left_size = mid - il
            root.left = dfs(pl,pl+left_size-1,il,mid-1)
            root.right = dfs(pl+left_size,pr-1,mid+1,ir)
            return root
        return dfs(0,len(postorder)-1,0,len(inorder)-1)