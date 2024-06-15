# https://leetcode.cn/problems/total-distance-traveled/

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = 0
        while mainTank>=5:
            t = mainTank // 5
            res += t * 5
            mainTank %= 5
            t = min(t, additionalTank)
            mainTank += t
            additionalTank -= t
        return (res + mainTank) * 10

# https://leetcode.cn/problems/water-bottles
    
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        while numBottles >= numExchange:
            t = numBottles // numExchange
            res += t * numExchange
            numBottles %= numExchange
            numBottles += t
        return res + numBottles