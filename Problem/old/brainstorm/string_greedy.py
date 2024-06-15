from typing import List


# https://leetcode.cn/problems/maximum-binary-string-after-change
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # 至多只有一个零，找到那个零的位置即可
        # 除了前排1，0后面1 可以挪动到末尾，其余的00000 -> 11110
        first_zero = binary.find('0')
        print(first_zero)
        if first_zero == -1:
            return binary
        nxt_zero = first_zero + binary[first_zero:].count('0') - 1
        return '1'*nxt_zero + '0' + '1' *(len(binary)-nxt_zero-1)