'''
Author: Puffrora
Date: 2020-12-09 15:38:34
LastModifiedBy: Puffrora
LastEditTime: 2020-12-09 15:47:31
'''


class Solution:
    def maximumSum(self, arr):

        # not_delete[i] 记录在 i 位置时不删除元素的连续数组最大和
        not_delete = [0] * len(arr)
        # delete[i] 记录在 i 位置时删除一个元素的连续数组最大和
        delete = [0] * len(arr)
        not_delete[0], delete[0] = arr[0], arr[0]
        res = arr[0]

        for i in range(1, len(arr)):
            not_delete[i] = max(not_delete[i-1]+arr[i], arr[i])
            delete[i] = max(delete[i-1]+arr[i], not_delete[i-1])

            res = max(res, max(not_delete[i], delete[i]))

        return res 

