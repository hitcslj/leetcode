'''
云上故障逃生

在云上多个业务节点之间选择最快的逃生节点集，并考虑每个节点的剩余业务容量。有一个网络时延表，表示每个节点到其他节点的通信延迟；还有一个剩余业务容量表，表示每个节点的剩余业务容量。在一个节点故障时，需要选择一个或多个逃生节点，确保逃生路径的时延最小，并且逃生节点集各节点剩余容量的总和足够容纳故障节点的业务量，当故障节点与多个节点最短距离相同，优先选择编号较小的节点容灾，如果逃生节点集中多个节点最短距离相同时按编号从小到大的顺序排列。


解答要求

时间限制: C/C++ 1000ms, 其他语言：2000ms
内存限制: C/C++ 256MB, 其他语言：512MB

输入

第1行n表示云上业务节点数， 2<=n<=10000，节点编号从 0 开始，依次递增；
第2到1+n行表示业务节点间的网络时延矩阵表 delayMatrix，delayMatrix[i][j] 表示节点 i 到节点 j 的通信时延;
1）如果节点 i 和节点 j 之间没有直接相连的边，则 delayMatrix[i][j] 为 -1，第i个节点和它自己也没有边，所以delayMatrix[i][i]=-1
2）节点间有边时延范围为 1<=delayMatrix[i][j]<=1000，矩阵元素间使用空格分割
另，输入保证 delayMatrix[i][j] == delayMatrix[j][i]
第2+n行表示各业务节点的剩余容量表 remainingCapacity，其中 remainingCapacity[i] 表示节点 i 的剩余业务容量，业务量的范围1<=�����������������[�]<=1001<=remainingCapacity[i]<=100，数组元素间使用空格分割；
第3+n行表示故障业务节点编号 faultyNode，表示发生故障的节点，取值范围为 0<=faultyNode<=n−1 ；
第4+n行表示受损业务节点需要迁移的业务量, 受损业务量的范围 (0−1000](0−1000] 。
输出

返回符合条件的逃生路径节点编号列表（以单空格间隔），当所有节点都不够故障节点业务容灾的时候输出所有容灾节点。

风险云服务个数
Example

input:
4 
-1 5 -1 8 
5 -1 1 3 
-1 1 -1 4 
8 3 4 -1 
10 20 15 25 
2 
12

output:
1

explain:
在给定的测试用例中，假设节点2发生故障，需要迁移业务量为12。节点2到其它节点的最短路径如下：
离故障节点2时延排序为1,3,0，故障节点要转移的业务量为12，而节点1的可容灾余量为20，足够容纳故障节点2的受灾业务，所以该测试用例的期望输出是 1。

input:
4 
-1 5 -1 8 
5 -1 1 3 
-1 1 -1 4 
8 3 4 -1 
10 20 15 25 
2 
50

output:
1 3 0

explain:
在给定的测试用例中，假设节点2发生故障，需要迁移业务量为50。节点2到其它节点的最短路径如下：
离故障节点2时延排序为1,3,0，故障节点要转移的业务量为50，而节点1的可容灾余量为20，不够容纳故障节点2的受灾业务30，所以还需找离节点2次近的节点3，节点3的可容灾余量为25，节点1的可容灾余量20和节点3的可容灾余量25的总和为45小于故障量50，需要增加0节点来容灾，，节点0的容灾余量为10，节点1,3,0总容灾余量为55，大于受灾节点的业务量50，所以该测试用例的期望输出是 1 3 0。


'''

from heapq import heappush, heappop

def main():
    n = int(input())
    delayMatrix = []
    for i in range(n):
        delayMatrix.append(list(map(int, input().split())))
    remainingCapacity = list(map(int, input().split()))
    faultyNode = int(input())
    faultyCapacity = int(input())
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if delayMatrix[i][j] != -1:
                g[i].append((j, delayMatrix[i][j]))
    def dijkstra(start):
        dist = [-1]*n
        dist[start] = 0
        q = [(0, start)]
        while q:
            d, u = heappop(q)
            if dist[u] < d: continue
            for v, w in g[u]:
                if dist[v] == -1 or d + w < dist[v]:
                    dist[v] = d + w
                    heappush(q, (dist[v], v))
        return dist
    dist = dijkstra(faultyNode)
    ans = []
    candidate = []
    for i in range(n):
        if i == faultyNode: continue
        candidate.append((dist[i], i))
    candidate.sort()
    for d,i in candidate:
        if faultyCapacity >= 0:
            faultyCapacity -= remainingCapacity[i]
            ans.append(i)
        else:
            break
    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    main()