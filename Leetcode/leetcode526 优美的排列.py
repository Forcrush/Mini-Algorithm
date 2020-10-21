'''
Author: Puffrora
Date: 2020-10-21 09:33:22
LastModifiedBy: Puffrora
LastEditTime: 2020-10-21 09:49:16
'''


class Solution:
    def countArrangement(self, N):
        cnt = 0
        arr = [i+1 for i in range(N)]

        def find(arr, pos):
            nonlocal cnt
            if pos == len(arr):
                cnt += 1
            
            for i in range(pos, len(arr)):
                arr[i], arr[pos] = arr[pos], arr[i]
                if arr[pos] % (pos + 1) == 0 or (pos + 1) % arr[pos] == 0:
                    find(arr, pos+1)
                arr[i], arr[pos] = arr[pos], arr[i]

        find(arr, 0)
        
        return cnt
