# Problem: 二分查找
def solve(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    path = ['S']
    d = 0
    while left <= right:
        mid = (left+right)//2
        d += 1
        if nums[mid] == target:
            return path + ['Y']
        elif nums[mid] < target:
            # if len(nums) < (1<<d):break
            path.append('R')
            left = mid + 1
        else:
            # if len(nums) < (1<<d):break
            path.append('L')
            right = mid - 1
    return path + ['N']


'''
input: 
4 2 1 3 6 5 7
5
output:
SRLY

input: 
2 1 3 7 5 6 4
6
output:
SRY

'''

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    target = int(input())
    ans = solve(nums, target)
    print(''.join(ans))