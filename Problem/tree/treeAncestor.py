from typing import List

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