# https://leetcode.cn/problems/trapping-rain-water-ii
from typing import List
from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap)<=2 or len(heightMap[0])<=2:
            return 0
        m,n = len(heightMap),len(heightMap[0])
        visited = [[False]*n for _ in range(m)]
        h = []
        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    heappush(h,(heightMap[i][j],i,j))
                    visited[i][j] = True
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        ans = 0
        while h:
            height,i,j = heappop(h)
            for dx,dy in dirs:
                x,y = i+dx,j+dy
                if 0<=x<m and 0<=y<n and not visited[x][y]:
                    if height>heightMap[x][y]:
                        ans += height-heightMap[x][y]
                    heappush(h,(max(height,heightMap[x][y]),x,y))
                    visited[x][y] = True
        return ans