'''
Author: Puffrora
Date: 2021-01-24 20:24:54
LastModifiedBy: Puffrora
LastEditTime: 2021-01-24 20:44:38
'''


class Solution:
    def makeArrayIncreasing(self, arr1, arr2):

        import bisect

        arr1 = [float('-inf')] + arr1 + [float('inf')]
        arr2 = sorted(list(set(arr2)))

        n = len(arr1)
        #  dp[i] 为使数组 arr1[0] 到 arr1[i] 递增且不替换 arr1[i] 的情况下的最小替换次数
        dp = [0] + [float('inf')] * (n - 1)

        for i in range(1, n):
            # 不替换 arr1[i-1]
            if arr1[i-1] < arr1[i]:
                dp[i] = min(dp[i], dp[i-1])

            # 替换 arr1[i-1] 以及之前的元素
            j = bisect.bisect_left(arr2, arr1[i])
            # 枚举替换的个数 [1, min(i-1, j)]
            for k in range(1, min(i-1, j)+1):
                # ! 当替换了 k 此后只有当 arr1[i-k-1] < arr2[j-k] 才可以保证序列递增
                if arr1[i-k-1] < arr2[j-k]:
                    dp[i] = min(dp[i], dp[i-k-1]+k)
        
        return dp[-1] if dp[-1] != float('inf') else -1
