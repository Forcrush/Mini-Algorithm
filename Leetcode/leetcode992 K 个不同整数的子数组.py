'''
Author: Puffrora
Date: 2020-12-08 08:56:21
LastModifiedBy: Puffrora
LastEditTime: 2020-12-08 17:17:43
'''


# 时间复杂度 O(N)
# 空间复杂度 O(K)
class Solution:
    def subarraysWithKDistinct(self, A, K):

        from collections import defaultdict

        # 计算最多含 K 个不同元素的子数组个数
        def atMostK(A, K):
            res, start = 0, 0
            window = defaultdict(int)
            for end in range(len(A)):
                if window[A[end]] == 0:
                    K -= 1
                window[A[end]] += 1

                while K < 0:
                    window[A[start]] -= 1
                    if window[A[start]] == 0:
                        K += 1
                    start += 1
                
                res += end - start + 1
        
            return res

        return atMostK(A, K) - atMostK(A, K-1)
        
        
