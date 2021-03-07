'''
Author: Puffrora
Date: 2021-03-07 11:39:20
LastModifiedBy: Puffrora
LastEditTime: 2021-03-07 18:05:52
'''


from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        res = left = 0
        while left < n - 2:
            right = left + 1
            if arr[left] < arr[right]:
                while right < n - 1 and arr[right] < arr[right+1]:
                    right += 1
                if right < n - 1 and arr[right] > arr[right+1]:
                    while right < n - 1 and arr[right] > arr[right+1]:
                        right += 1
                    res = max(res, right-left+1)
                else:
                    right += 1
            left = right
        return res
