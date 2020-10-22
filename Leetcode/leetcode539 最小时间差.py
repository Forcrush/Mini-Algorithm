'''
Author: Puffrora
Date: 2020-10-21 23:35:24
LastModifiedBy: Puffrora
LastEditTime: 2020-10-21 23:58:23
'''


# 映射成分钟后排序
# 时间复杂度 O(NlogN)
# 空间复杂度 O(1)
class Solution:
    def findMinDifference(self, timePoints):
        for i in range(len(timePoints)):
            hour, minute = list(map(int, timePoints[i].split(':')))
            timePoints[i] = 60 * hour + minute
        
        timePoints.sort()
        
        res = float('inf')
        for i in range(1, len(timePoints)):
            if timePoints[i] - timePoints[i-1] < res:
                res = timePoints[i] - timePoints[i-1]
                
        return min(res, min(timePoints[-1] - timePoints[0], 1440 + timePoints[0] - timePoints[-1]))


print(Solution().findMinDifference(["23:59", "00:00"]))
# 哈希表 映射成分钟并将分钟值作为下标
# 时间复杂度 O(N)
# 空间复杂度 O(N)
# . Easy to implement...
