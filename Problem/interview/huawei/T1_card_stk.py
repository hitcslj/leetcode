'''
扑克牌消除

从一副扑克牌中随机抽取n张牌组成一个序列，规定连续3张相同牌号的卡牌可以消除，剩余卡牌按照当前顺序重新合并成新的序列后继续消除，重复以上步骤直到无法消除，最后请输出结束后剩余的卡牌序列。
注：存在连续4张相同牌号的情况，消除后剩余一张。
解答要求

时间限制: C/C++ 1000ms, 其他语言：2000ms
内存限制: C/C++ 256MB, 其他语言：512MB
输入

第一行一个正整数n（1 ≤n ≤ 52），表示卡牌的数量。第二行一个字符串，以空格分隔代表卡牌号序列，卡牌号仅包含2-10，A，J，Q，K。
输出

一个字符串，打印最终结束后的卡牌号序列，卡牌号以空格分隔。如果最终没有卡牌剩余输出0。

example:
input:
10
3 A 2 2 2 A A 7 7 7
output:
3
'''

n = len(input())
cards = input().split(" ")
stack = []
for i, card in enumerate(cards):
    stack.append(card)
    while stack>=3 and  stack[-1] == stack[-2] == stack[-3]:
        stack.pop()
        stack.pop()
        stack.pop()
if len(stack) == 0:
    print(0)
else:
    print(' '.join(stack))
