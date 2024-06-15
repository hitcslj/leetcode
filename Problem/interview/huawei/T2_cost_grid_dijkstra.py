import heapq
from math import inf

# 双向dijkstra 
def solve(ci, cj):
    visited = [[False] * m for _ in range(n)]
    dis = [[inf] * m for _ in range(n)]
    dis[ci][cj] = 0
    q = []
    heapq.heappush(q, (0, ci, cj))
    while q:
        cost, i, j = heapq.heappop(q)
        if visited[i][j]:continue
        visited[i][j] = True
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and matrix[ni][nj] != 'B':
                w = 0
                if matrix[ni][nj] in 'CSE':
                    w = 0
                else:
                    w = int(matrix[ni][nj])
                if dis[ni][nj] > cost + w:
                    dis[ni][nj] = cost + w
                    heapq.heappush(q, (dis[ni][nj], ni, nj))
    return dis


'''
input:
3 3
S 4 5
7 B 3
C 9 E

output:
16
'''
if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(input().split()))
    C = []
    res = inf
    si,sj,ei,ej = 0,0,0,0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'S':
                si, sj = i, j
            elif matrix[i][j] == 'E':
                ei, ej = i, j
            elif matrix[i][j] == 'C':
                C.append((i, j))
    for ci,cj in C:
        dis = solve(ci,cj)
        if dis[si][sj] == inf or dis[ei][ej] == inf:
            continue
        else:
            res = min(res, dis[si][sj] + dis[ei][ej])
    if res == inf:
        print(-1)
    else:
        print(res)