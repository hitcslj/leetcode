# https://leetcode.cn/problems/snapshot-array
from collections import defaultdict
from bisect import bisect_left

class SnapshotArray:
    def __init__(self, _: int):
        self.cur_snap_id = 0
        self.history = defaultdict(list)  # 每个 index 的历史修改记录

    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.cur_snap_id, val))

    def snap(self) -> int:
        self.cur_snap_id += 1
        return self.cur_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # 找快照编号 <= snap_id 的最后一次修改记录
        # 等价于找快照编号 >= snap_id+1 的第一个修改记录，它的上一个就是答案
        j = bisect_left(self.history[index], (snap_id + 1,)) - 1
        return self.history[index][j][1] if j >= 0 else 0