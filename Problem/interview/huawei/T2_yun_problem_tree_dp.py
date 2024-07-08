'''
计算云服务DI值

我们将云服务看做一棵树，每个云服务在发布前尚未解决的问题称为云服务的遗留问题（云服务的遗留问题包含以该云服务为根节点的树上所有节点的问题），DI值（遗留问题缺陷密度）可以作为评估云服务发布的指标，当云服务DI值小于等于阈值时才准许云服务发布，否则视为风险云服务，需要问题整改完成后重新进行发布评估。现有一批云服务树，已给出云服务树各节点的问题数量，请通过计算输出风险云服务的个数。
计算公式：DI值≤5×严重问题数＋2×一般问题数，其中每个节点的不同级别问题数量需要将该节点及该节点为根节点的所有子节点的相应级别问题数量求和。
解答要求

时间限制: C/C++ 1000ms, 其他语言：2000ms
内存限制: C/C++ 64MB, 其他语言：128MB
输入

第一行输入M和N(M≤100000，N≤1000)，使用空格分隔，M表示代表云服务阈值，N表示接下来有N行问题统计数据；
接下来输入一个N∗4的矩阵表，行内使用空格分隔，第一列Ai为服务节点，第二列Bi为Ai的父节点，如果Ai为云服务则无父节点，此时Bi用∗号表示(Ai和Bi取值为字符串，1≤字符串长度≤5，均由小写英文字母或∗号组成)，第三列Ci为问题级别（Ci取值为{0,1}，0表示严重问题，1表示一般问题），第四列Di为该节点该级别的问题数量(Di≤1000)。
说明：输入保证只出现树的关系，不会出现连通图的情况。
输出

风险云服务个数
Example

input:
40 12 
a * 0 2 
a * 1 2 
b a 0 3 
b a 1 5 
c a 1 3 
d a 0 1 
d a 1 3 
e b 0 2 
f * 0 8 
f * 1 10 
g f 1 2
h * 0 4

output:
2

explain:
a * 0 2表示节点a有2个严重问题，*表示无父节点，即a为云服务。b a 1 5表示节点b有5个一般问题，b的父节点是a。可以看出，该样例有3个云服务a、f、h。云服务a的子节点有b、c、d、e，严重问题个数为2+3+0+1+2=82+3+0+1+2=8，一般问题个数为2+5+3+3+0=132+5+3+3+0=13，DI值=8∗5+13∗2=66>阈值40，故云服务a是风险云服务；云服务f严重问题个数为8+0=88+0=8，一般问题个数为10+2=1210+2=12，DI值=8∗5+12∗2=64>阈值40，故云服务f也是风险云服务；云服务h严重问题个数为44，一般问题个数为00，DI值=4∗5+0∗2=20<=阈值40，故云服务h不是风险云服务；因此该样例有2个风险云服务。
'''

from collections import defaultdict

def main():
    m, n = map(int, input().split())
    threshold = m
    g = defaultdict(set)
    p0 = defaultdict(int)
    p1 = defaultdict(int)
    for _ in range(n):
        a,b,c,num = input().strip().split(" ")
        num = int(num)
        g[b].add(a)
        if c == '0':
            p0[a]=num
        else:
            p1[a]=num
    
    def dfs(x):
        cnt = [0]*2
        cnt[0] += p0[x]
        cnt[1] += p1[x]
        for y in g[x]:
            cnt[0] += dfs(y)[0]
            cnt[1] += dfs(y)[1]
        return cnt
    ans = 0
    for x in g['*']:
        cnt = dfs(x)
        if cnt[0]*5 + cnt[1]*2 > threshold:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()