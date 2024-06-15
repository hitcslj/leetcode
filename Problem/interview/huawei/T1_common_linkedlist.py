# 找到最长公共子串
def longest_common_substring(arr1, arr2):
    # 获取两个数组的长度
    len1, len2 = len(arr1), len(arr2)
    
    # 初始化动态规划表
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    # 记录最长公共子串的最大长度和结束位置
    max_length = 0
    end_index = 0
    
    # 填充动态规划表
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0
    
    # 提取最长公共子串
    longest_substring = arr1[end_index - max_length: end_index]
    return longest_substring


# 示例
'''
input: 
1 2 2 3 9 1 5
9 2 2 3 6 8

output:
2 2 3
'''
if __name__ == "__main__":
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    res = longest_common_substring(nums1, nums2)
    if len(res) == 0:
        print(-1)
    else:
        print(*res)
