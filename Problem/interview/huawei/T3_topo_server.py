'''
找到内聚值最大的微服务群组

开发团队为了调研微服务调用情况,对n个微服务调用数据进行了采集分析,微服务使用数字0至n-1进行编号，给你一个下标从0开始的数组edges , 其中edges[i]表示存在一条从微服务i到微服务edges[i]的接口调用。
我们将形成1个环的多个微服务称为微服务群组，一个微服务群组的所有微服务数量为L，能够访问到该微服务群组的微服务数量为V,这个微服务群组的内聚值H=L-V.
已知提供的数据中有1个或多个微服务群组，请按照内聚值H的结果从大到小的顺序对所有微服务群组(（H相等时，取环中最大的数进行比较)排序，输出排在第一的做服务群组，输出时每个微服务群组输出的起始编号为环中最小的数。
输入
入参分为两行输入: 第一行为n,表示有n个微服务 第二行为数组edges,其中edges[i]表示存在一条从微服务i到微服务edges[i]的接口调用，数字以空格分隔
输入范围说明: n== edges.length 2<= n <=10^5 0  <= edges[i] <= n-1
edges[i] !=i
输出
输出排在第一的微服务群组的编号数组，按照环的访问顺序输出，起始编号为环中最小的数,数字以空格分隔

example:
input:
4
3 3 0 2
ouput:
0 3 2

input:
12
2 6 10 1 6 0 3 0 5 4 5 8
output:
0 2 10 5


'''



from collections import deque


def main():
    n = int(input())
    edges = list(map(int, input().split()))
    in_degree = [0] * n
    nums = [0] * n

    # 计算每个节点的入度
    for i in range(n):
        in_degree[edges[i]] += 1

    # 初始化队列，将入度为0的节点加入队列
    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    # 拓扑排序处理入度为0的节点
    while q:
        f = q.popleft()
        in_degree[edges[f]] -= 1
        nums[edges[f]] += nums[f] + 1
        if in_degree[edges[f]] == 0:
            q.append(edges[f])

    cir = []
    value = []
    mx = []

    # 处理环的节点
    for i in range(n):
        if in_degree[i] == 0:
            continue
        c = i
        v = 0
        mx_no = i
        path = []
        while in_degree[c]:
            v += nums[c]
            path.append(c)
            in_degree[c] = 0
            c = edges[c]
            mx_no = max(mx_no, c)
        cir.append(path)
        mx.append(mx_no)
        value.append(len(path) - v)

    # 排序环节点
    idx = list(range(len(value)))
    idx.sort(key=lambda x: (value[x], mx[x]), reverse=True)

    # 选择最佳路径
    path = cir[idx[0]]
    start = min(path)

    result = []
    for _ in range(len(path)):
        result.append(str(start))
        start = edges[start]

    print(" ".join(result))

if __name__ == "__main__":
    main()
