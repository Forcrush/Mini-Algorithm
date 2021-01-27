'''
Author: Puffrora
Date: 2021-01-27 13:03:56
LastModifiedBy: Puffrora
LastEditTime: 2021-01-27 13:17:20
'''


class Solution:
    def makesquare(self, nums):
        
        if sum(nums) % 4: return False

        target = sum(nums) // 4
        visited = [0] * len(nums)

        # start为搜索起点 cursum为目前子集和 cnt为目前使用过的数字数量
        def dfs(k, start, cursum, cnt):
            if k == 1:
                return True
            if cursum == target and cnt > 0:
                return dfs(k-1, 0, 0, 0)
            for i in range(start, len(nums)):
                if not visited[i] and cursum + nums[i] <= target:
                    visited[i] = 1
                    if dfs(k, i+1, cursum+nums[i], cnt+1):
                        return True
                    visited[i] = 0
            
            return False
        
        return dfs(4, 0, 0, 0)


