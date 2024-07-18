# https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
        if num == 1:
            return 0
        return (self.iceBreakingGame(num-1,target) + target) % num
    
# https://leetcode.cn/problems/elimination-game
class Solution:
    def lastRemaining(self, n: int) -> int:
        if n <= 2: return n
        return 2*(n//2+1-self.lastRemaining(n//2))