from typing import List
from collections import Counter
import string

# 比赛时用于调试的代码
class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        n //= 2
        l,r = s[:n],s[n:][::-1]
        # 计数前缀和
        # Counter前缀和
        pre_a = [Counter() for _ in range(n+1)]
        pre_b = [Counter() for _ in range(n+1)]
        
        for i,w in enumerate(l):
            pre_a[i+1] = pre_a[i].copy()
            pre_a[i+1][w] += 1
        
        for i,w in enumerate(r):
            pre_b[i+1] = pre_b[i].copy()
            pre_b[i+1][w] += 1
        
        base, mod = 1331, 10**20 + 7
        # 滚动哈希前缀和
        def getHashPre(s):
            n = len(s)
            
            # hash前缀和
            pre_hash = [0] * (n+1)
            # 指数数组
            # pow_arr[i] 代表 mul 的 i 次方
            pow_arr = [0] * (n+1)
            # 可以使用两个mod组成二元组编码，防止hash碰撞
            # 或者mod足够大。。      
            tmp = 0
            mul = 1                                
            for i in range(n):
                tmp = (tmp * base + ord(s[i])) % mod
                pre_hash[i+1] = tmp
                pow_arr[i] = mul                 
                mul = mul * base % mod
            pow_arr[n] = mul
            return pre_hash,pow_arr
        
        
        pre_hash_a,pow_arr = getHashPre(l)
        pre_hash_b,_ = getHashPre(r)
        
        # 获取[l,r)的hashcode值，长度为r-l
        def getHash(pre_hash,l,r):
            return ((pre_hash[r] - pre_hash[l] * pow_arr[r-l])%mod + mod)%mod 
        
        res = []
        
        # 判断范围内计数是否相等
        def checkCnt(pre_a,pre_b,l,r):
            if l > r:
                return True
            
            for w in string.ascii_lowercase:
                if pre_a[r+1][w] - pre_a[l][w] != pre_b[r+1][w] - pre_b[l][w]:
                    return False
            return True
        
        # 默认[a,b] <= [c,d]
        def getRes(pre_a,pre_b,pre_hash_a,pre_hash_b,a,b,c,d):
            left = min(a,c)
            if getHash(pre_hash_a,0,left) != getHash(pre_hash_b,0,left):
                return False
            
            right = max(b,d)
            if getHash(pre_hash_a,right+1,n) != getHash(pre_hash_b,right+1,n):
                return False
            
            if not checkCnt(pre_a,pre_b,a,max(b,d)):
                return False
            
            # 中间
            # 不重叠
            # a....b
            #         c...d
            if b < c:
                # 先计算中间
                if getHash(pre_hash_a,b+1,c) != getHash(pre_hash_b,b+1,c):
                    return False
                
                # cnt [a,b]
                if not checkCnt(pre_a,pre_b,a,b):
                    return False
                
                if not checkCnt(pre_a,pre_b,c,d):
                    return False
                
                return True
            # 重叠
            # a.....b
            #    c.....d
            elif b < d:
                for w in string.ascii_lowercase:
                    if pre_a[d+1][w] - pre_a[b+1][w] > pre_b[d+1][w] - pre_b[c][w]:
                        return False
                
                return True
            # 重叠覆盖
            # a........b
            #    c..d
            else:
                return True
                
        
        for a,b,c,d in queries:
            c -= n
            d -= n
            c = n - 1 - c
            d = n - 1 - d
            c,d = d,c
            # print(a,b,c,d)
            
            if a > c:
                res.append(getRes(pre_b,pre_a,pre_hash_b,pre_hash_a,c,d,a,b))
            else:
                res.append(getRes(pre_a,pre_b,pre_hash_a,pre_hash_b,a,b,c,d))
        
        return res


s = "abcabc"
queries = [[1,1,3,5],[0,2,5,5]]

print(Solution().canMakePalindromeQueries(s,queries)) # [True,True]