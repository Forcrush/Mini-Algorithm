'''
Author: Puffrora
Date: 2020-10-08 18:11:20
LastModifiedBy: Puffrora
LastEditTime: 2020-10-08 18:19:15
'''


# 时间复杂度 O(N)
# 空间复杂度 O(N)
class Solution:
    def subarraySum(self, nums, k):
        from collections import defaultdict

        dic = defaultdict(int)
        dic[0] = 1
        cur_sum = 0
        cnt = 0

        for n in nums:
            cur_sum += n
            cnt += dic[cur_sum - k]
            dic[cur_sum] += 1
        
        return cnt
