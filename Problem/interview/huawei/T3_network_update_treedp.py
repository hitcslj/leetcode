'''
网络升级改造
由于软件技术的提升，原有部署网络中某些节点可以撤掉，这样可以简化网络节省维护成本。但是要求撤掉网络节点时，不能同时撤掉原来两个直接相互连接的节点。
输入的网络是一个满二叉树结构，每个网络节点上标注一个数值，表示该节点的每年维护成本费用。
给定每个输入网络，按照要求撤掉某些节点后，求出能够节省的最大的维护成本


input:
7
5 3 5 0 6 0 1
output:
12
expain:
第一行输入:7，表示后面有7个数值
第二行输入:5 3 5 0 6 0 1，表示“表示网络节点每年的维护成本，按照满二又树的度优先遍历序号”给出。
输出：12，能够节省的最大维护成本：5+6+1

'''

from functools import cache
def main():
    n = int(input())
    nums = list(map(int, input().split()))
    # 打家劫舍问题
    @cache
    def dfs(i):
        if i >= n:
            return [0,0]  # 选 or 不选
        l = dfs(i * 2 + 1)
        r = dfs(i * 2 + 2)
        return [nums[i] + l[1] + r[1], max(l) + max(r)]
    print(max(dfs(0)))

if __name__ == '__main__':
    main()