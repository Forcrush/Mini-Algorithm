'''
Author: Puffrora
Date: 2021-03-01 11:23:42
LastModifiedBy: Puffrora
LastEditTime: 2021-03-01 14:45:55
'''


# 枚举
# 时间复杂度 O(√N)
# 空间复杂度 O(1)
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if num == 1: return False
        
        threshold = int(num ** 0.5)
        res = 1
        for i in range(2, threshold+1):
            if num % i == 0:
                res += i
                res += num // i
        
        return res == num


# 欧几里得-欧拉定理
# 时间复杂度 O(1)
# 空间复杂度 O(1)
"""
每个偶完全数都可以写成 2^(p-1) * (2^p - 1) 的形式，其中 p 为素数
由于目前奇完全数还未被发现 因此所有的完全数都可以写成上述形式 当 n 不
超过 10^8 时 p 也不会很大 因此我们只要带入最小的若干个素数 2, 3, 5, 
7, 13, 17, 19, 31 将不超过 10^8 的所有完全数计算出来即可
"""
class Solution1:
    def checkPerfectNumber(self, num: int) -> bool:

        def p_complete(p):
            return (1<<(p-1)) * ((1<<p) - 1)

        for p in [2, 3, 5, 7, 13, 17, 19, 31]:
            if p_complete(p) == num:
                return True
        
        return False