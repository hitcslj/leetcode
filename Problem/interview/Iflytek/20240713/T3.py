'''
乘2除2

给出一个大小为n的序列a，每次操作可以选择序列a中的一个数x，把x变成x*2或者[x/2]（对同一个a可以操作多次但不能既进行乘操作又进行除操作）。
问最少操作多少次使得a是不下降的。
输入描述
第一行输入一个整数n。(1<=n<=20000) 第二行输入n个整数表示序列a。(1<=ai<=20000)
输出描述
输出一行一个整数表示答案。
示例 1
输入
5
10 10 5 6 4
输出
3
说明
最终序列为[5,5,5,6,8]
示例 2
输入
8
10 3 1 6 8 12 7 5
输出
7
'''

import sys
from collections import defaultdict

MAXN = 10**18

def min_operations_to_non_decreasing(nums):
    n = len(nums)
    dp = [defaultdict(lambda: sys.maxsize) for _ in range(n + 1)]
    dp[0][1] = 0

    for i in range(n):
        for j, steps in dp[i].items():
            if nums[i] >= j:
                # 不变
                if dp[i + 1][nums[i]] > steps:
                    dp[i + 1][nums[i]] = steps
                
                # 变大
                num = nums[i]
                cnt = 0
                while num <= MAXN:
                    num *= 2
                    cnt += 1
                    if dp[i + 1][num] > steps + cnt:
                        dp[i + 1][num] = steps + cnt
                    if num > MAXN / 2:
                        break
                
                # 变小
                num = nums[i]
                cnt = 0
                while num // 2 >= j:
                    cnt += 1
                    num //= 2
                    if dp[i + 1][num] > steps + cnt:
                        dp[i + 1][num] = steps + cnt
            else:
                # 只能变大
                num = nums[i]
                cnt = 0
                while num <= MAXN:
                    num *= 2
                    cnt += 1
                    if num >= j and dp[i + 1][num] > steps + cnt:
                        dp[i + 1][num] = steps + cnt
                    if num > MAXN / 2:
                        break

    ans = sys.maxsize
    for k, v in dp[n].items():
        if v < ans:
            ans = v

    return ans

# 示例用法
n = int(input().strip())
nums = list(map(int, input().strip().split()))

result = min_operations_to_non_decreasing(nums)
print(result)
