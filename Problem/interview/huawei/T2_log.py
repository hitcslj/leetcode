'''
海量日志抑制

程序运行日志是重要的运维手段，需要尽量记录下有效信息，避免无效日志，
而”海量日志”就是一种比较典型的日志使用问题——大量打印相同或相似的内容，将有效日志淹没，还可能降低系统运行效率。
因此，需要“海量日志”抑制机制，避免系统运行时产生“海量日志”问题。
海量日志”定义: 
10ms内(<10ms)打印2条相同日志 (包含第2条均需要被抑制)，即:仅保留第一条或
100ms内(<100ms)打印10条相似日志(去除数字后完全相同的两条日志认为是“相似”，包含第10条均需要被抑制)，即:仅保留前9条。
日志抑制的理解:被抑制的日志，不记录到日志文件中

输入
本用例的日志条数(最大不超过1000条) 时间截:日志打印内容

约束
1、时间戳单位是ms，用32位无符号+进制整数表示
2、用例保证后一条日志时间戳不小于前一条;
3、一条日志打打印只占一行，一条日志内容不超过1024 Bytes;
4、用例保证1s内(<1s)，最多100条日志
5、数字均为正整数。

输出
时间戳:日志打印内容 输出需要除去被抑制的日志

example:
input:
4
123 This is a log
123 This is a log
136 This is a new log   
138 This is a new log

output:
123 This is a log
136 This is a new log


expain:
第二条”123 This is alog”、以及”138 This is a new log”被抑制，抑制廉因为满足”相同日志“抑制规则
'''

from collections import defaultdict
import re

def main():
    n = int(input())
    records = []
    same = defaultdict(list)
    like = defaultdict(list)
    vst = [True] * n
    for i in range(n):
        lines = input().strip().split(" ")
        time = int(lines[0])
        text = ' '.join(lines[1:])
        same[text].append([time, i])
        like[re.sub(r'\d','', text)].append([time, i])
        records.append(' '.join(lines))
    for d in same:
        record = same[d] # time index
        for i,rec in enumerate(record):
            time, index = rec
            if i+1<len(record) and record[i+1][0] - time < 10: vst[record[i+1][1]] = False

    for d in like:
        record = like[d]  # time index
        for i, rec in enumerate(record):
            time, index = rec
            if i + 10 < len(record) and record[i + 10][0] - time < 10: vst[record[i + 10][1]] = False
    for i, record in enumerate(records):
        if vst[i]: print(record)


if __name__ == '__main__':
    main()