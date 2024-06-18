'''
疯长的草
将N种不同的随机种在一块广漠无边的二维平面上(角坐标系内)，给定二维数组points表示第0天所有草的初始位置，
第i项points[I]=[XI,Y]表示第0天草i点[XI,YI].每天被草覆盖的点会向外蔓延到它上、下、左、右、左上、左下、右上、右下8个邻居点。
注意，初始状态下，可能有多种草在同一点上。
现给定一个整数 M，问最少需要多少天，方能找到一点同时至少有 M 种草?
输入
第一行输入整数M。(2 <= M <= n)
第二行输入草的种数n。(2 <= n <= 50)
后面连续n行输入草i初始位置[xi, yi]。(1 <= xi,yi <= 10^9)
输出
返回找到一点至少生长 M 种草的最少天数，找不到返回0

example:
Input:
2
2
2 1
6 2
Output:
2

Input:
2
3
2 1
6 2
100 100
Output:
2
Explain:


提示
n = points.length
2 <= n <= 50
points[I].length = 2 1 <= xi,Yi <= 10^9 2 <= M <=n


'''

def main():
    m = int(input())
    n = int(input())
    xys = []
    for i in range(n):
        x, y = map(int, input().split())
        xys.append([x, y])
    res = -1
    r = int(1e9 + 1)
    l = 0

    def check(mid):
        ls = []
        # 得到矩形的左下角和右上角坐标
        for x,y in xys:
            ls.append([x-mid,y-mid,x+mid,y+mid])
        # 扫描线，判断是否存在一个点至少被m种矩形覆盖
        
        
    while l <= r:
        mid = (l + r) // 2
        if check(mid): # 在mid天内可以找到k种草
            res=mid
            r = mid - 1
        else:
            l = mid + 1

    if res == -1:
        print(0)
    else:
        print(res)

if __name__ == '__main__':
    main()