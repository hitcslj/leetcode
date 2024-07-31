from typing import List


'''
最小区间覆盖

注意到对于所有左端点相同的子区间，其右端点越远越有利。且最佳方案中不可能出现两个左端点相同的子区间。

于是我们预处理所有的子区间，对于每一个位置 i，我们记录以其为左端点的子区间中最远的右端点，记为 maxn[i]。

我们可以参考「55. 跳跃游戏的官方题解」，使用贪心解决这道题。

具体地，我们枚举每一个位置，假设当枚举到位置 i 时，记左端点不大于 i 的所有子区间的最远右端点为 last。

这样 last 就代表了当前能覆盖到的最远的右端点。

每次我们枚举到一个新位置，我们都用 maxn[i] 来更新 last。

如果更新后 last==i，那么说明下一个位置无法被覆盖，我们无法完成目标。

同时我们还需要记录上一个被使用的子区间的结束位置为 pre，每次我们越过一个被使用的子区间，就说明我们要启用一个新子区间，

这个新子区间的结束位置即为当前的 last。

也就是说，每次我们遇到 i==pre，则说明我们用完了一个被使用的子区间。这种情况下我们让答案加 1，并更新 pre 即可。

'''
# https://leetcode.cn/problems/video-stitching/solutions/458461/shi-pin-pin-jie-by-leetcode-solution/
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        maxn = [0] * time
        last = ret = pre = 0
        for a, b in clips:
            if a < time:
                maxn[a] = max(maxn[a], b)
        
        for i in range(time):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last
        
        return ret

# 合并区间
# https://leetcode.cn/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0]) #这里是按照开始端点排序
        merged = []
        for l,r in intervals:
            if not merged or merged[-1][1]<l:
                merged.append([l,r])
            else:
                merged[-1][1] = max(merged[-1][1],r)
        return merged

# 删除重叠区间
# https://leetcode.cn/problems/non-overlapping-intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]
        
        return n - ans

# 插入区间
# https://leetcode.cn/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left,right = newInterval
        placed = False
        res = []
        for l,r in intervals:
            if r<left:
                res.append([l,r])
            elif l>right:
                if not placed:
                    res.append([left,right])
                    placed = True
                res.append([l,r])
            else:
                left = min(left,l)
                right = max(right,r)
        if not placed:
            res.append([left,right])
        return res

 