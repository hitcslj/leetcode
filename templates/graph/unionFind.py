# https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/

from typing import List

class UnionFind:
    def __init__(self,n):
        self.pa = list(range(n))
        self.size = n
    def find(self,x):
        if x!=self.pa[x]:
            self.pa[x]=self.find(self.pa[x])
        return self.pa[x]
    
    def merge(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        if root_x != root_y:
            self.pa[root_x] = root_y
            self.size-=1


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        ## 并查集
        n = len(nums)
        uf = UnionFind(n)
        rank = sorted(range(n),key=lambda x:nums[x])
        for i in range(1,n):
            if nums[rank[i]]-nums[rank[i-1]]<=limit:
                uf.merge(rank[i],rank[i-1])
        cnt = defaultdict(list)
        for i,pa in enumerate(uf.pa):
            cnt[pa].append(i) # 把可以交换的放到一个联通块里
        newNums = nums[:]
        for arr in cnt.values():
            newArr = sorted(arr,key=lambda x:nums[x])
            for i in range(len(arr)):
                newNums[arr[i]] = nums[newArr[i]]
        return newNums


