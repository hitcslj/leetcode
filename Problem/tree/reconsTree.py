from typing import List,Optional
from functools import cache

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

# https://leetcode.cn/problems/all-possible-full-binary-trees
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dfs(n):
            if n%2==0:
                return []
            if n==1:
                return [TreeNode()]

            res =  []
            for lnum in range(1,n):
                ls = dfs(lnum)
                rs = dfs(n-1-lnum)
                for lt in ls:
                    for rt in rs:
                        res.append(TreeNode(0,lt,rt))
            return res
        
        return dfs(n)

# https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stk = []
        for c in preorder.split(','):
            stk.append(c)
            while len(stk)>2 and stk[-1]=='#' and stk[-2]=='#' and stk[-3]!='#':
                stk = stk[:-3]
                stk.append('#')

        return len(stk)==1 and stk[0]=='#'

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        n = len(preorder)  
        def dfs():
            nonlocal i,n
            # 如果节点用完了直接，返回False
            if i==n:return False
            if preorder[i]=='#':
                i += 1
                return True
            # root
            i += 1
            # lchild
            if not dfs():return False
            # rchild
            if not dfs():return False
            return True
        i = 0
        return dfs() and i == n

# https://leetcode.cn/problems/unique-binary-search-trees/
class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def dfs(left,right):
            if left > right: return 1
            ans = 0
            for root in range(left,right+1):
                ans += dfs(left,root-1)*dfs(root+1,right)
            return ans
        return dfs(1,n)

# https://leetcode.cn/problems/unique-binary-search-trees-ii/
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dfs(left,right):
            if left>right:return [None,]
            res = []
            for rootVal in range(left,right+1):
                    for l in dfs(left,rootVal-1):
                        for r in dfs(rootVal+1,right):
                            root = TreeNode(rootVal,l,r)
                            res.append(root)
            return res
        return dfs(1,n)