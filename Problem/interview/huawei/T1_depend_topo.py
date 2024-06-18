'''
批量初始化次数

某部门在开发一个代码分析工具，需要分析模块之间的依赖关系，用来确定模块的初始化顺序、是否有循环依期等问题。
"批量初始化”是指一次可以初始化一个或多个模块。例如模块1依赖模块2，模块3也依赖模块2，但模块1和3没有依赖关系，则必须先"批量初始化”模块2，再"批量初始化"模块1和3。现给定一组模块间的依赖关系，请计算需要“批量初始化"的次数。

输入
(1)第1行只有一个数字.表示模块总数N。
(2)随后的N行依次表示模块1到N的依赖数据。每行的第1个数表示依赖的模块数量(不会超过N)，之后的数字表示当前模块依赖的ID序列。该序列不会重复出现相同的数字，模块ID的取值定在[1,N]之内。
(3)模块总数N取值范围 1<=N<=1000.
(4)每一行里面的数字按1个空格分隔。
输出
输出"批量初始化次数”.若有循环依赖无法完成初始化，则输出-1。

Example
Input:
5
3 2 3 4
1 5
1 5
1 5 
0
output:
3
explain:
共5个模块。
模块1依赖模块2、3、4；
模块2依赖模块5
模块3依赖模块5
模块4依赖模块5
模块5没有依赖任何模块
批量初始化顺序为{5}->{2，3，4}->{1},共需”批量初始化”3次

Input:
3
1 2
1 3
1 1  
Output:
-1
explain:
存在循环依赖，无法完成初始化，返回-1
'''
from collections import deque

def main():
    n = int(input())
    g = [[] for _ in range(n)]
    indegree = [0] * n
    for i in range(n):
        line = list(map(int, input().split()))
        indegree[i] = line[0]
        for j in range(1, len(line)):
            g[line[j] - 1].append(i)
    res = cnt = 0
    q = deque([i for i in range(n) if indegree[i] == 0])

    while q:
        res += 1
        for _ in range(len(q)):
            u = q.popleft()
            cnt += 1
            for v in g[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
    if cnt != n:
        print('-1')
    else:
        print(res)

if __name__ == '__main__':
    main()

