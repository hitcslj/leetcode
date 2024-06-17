'''
球队有n个足球队员参与m次射门训练，每次射门进球用1表示，射失则用0表示，依据如下规则对该n个队员的射门能力做排序 1、进球总数更多的队员射门能力更强 2、若进球总数—样多，则比较最多—次连续进球的个数，最多的队员能力更强 3、若最多一次连续进球的个数一样多，则比较第一次射失的先后顺序，其中后射失的队员更强，若第一次射失顺序相同，则按继续比较第二次射失的顺序，后丢球的队员能术更强，依次类推 4、若前3个规则排序后还能力相等，则队员编号更小的能力更强
输入
第1行，足球队员数n，射门训练次数m。(队员编号从1开始，依次递增) 第2行，第1~n个队员从第1到m次训练的进球情况，每个队员进球情况为连续的1和0的组合，不同队员用空格分隔n和m均为正整数，0<n<=10 ^ 3，0<m<=10^3
输出
射门能力从强到弱的队员编号,用空格分隔


input:
4 5
11100 00111 10111 01111
output:
4 3 1 2

'''
from functools import cmp_to_key


def solve(n,m,strs):
    goals = [0] * n
    seq = [0] * n
    fs = [[] for _ in range(n)]
    
    for i in range(n):
        s = strs[i]
        g = 0
        mx_s = 0
        cur_s = 0
        for j in range(m):
            if s[j] == '1':
                g += 1
                cur_s += 1
            else:
                mx_s = max(mx_s, cur_s)
                fs[i].append(j)
                cur_s = 0
        goals[i] = g
        seq[i] = max(mx_s, cur_s)
    
    idx = list(range(n))
    
    def compare(a, b):
        if goals[a] > goals[b]:
            return -1
        if goals[a] < goals[b]:
            return 1
        if seq[a] > seq[b]:
            return -1
        if seq[a] < seq[b]:
            return 1
        for j in range(len(fs[a])):
            if fs[a][j] > fs[b][j]:
                return -1
            if fs[a][j] < fs[b][j]:
                return 1
        return a - b
    
    idx.sort(key=cmp_to_key(compare))
    
    ans = " ".join(str(i + 1) for i in idx)
    return ans


# 根据规则
# 1. 进球总数更多的队员射门能力更强
# 2. 若进球总数—样多，则比较最多—次连续进球的个数，最多的队员能力更强
# 3. 若最多一次连续进球的个数一样多，则比较第一次射失的先后顺序，其中后射失的队员更强，若第一次射失顺序相同，则按继续比较第二次射失的顺序，后丢球的队员能术更强，依次类推
# 4. 若前3个规则排序后还能力相等，则队员编号更小的能力更强
if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    strs = input().split()
    ans = solve(n,m,strs)
    print(ans)




            
