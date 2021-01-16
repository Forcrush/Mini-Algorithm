'''
Author: Puffrora
Date: 2021-01-16 21:10:19
LastModifiedBy: Puffrora
LastEditTime: 2021-01-16 21:38:10
'''


"""
dp[i] 表示放置前 i 本书所需要的书架最小高度遍历每一本书，把当前这本书作为书架
最后一层的最后一本书，将这本书之前的书向后调整，看看是否可以减少之前的书架高度

!!! 摆放书的顺序与整理好的顺序(books列表顺序)相同
"""
class Solution:
    def minHeightShelves(self, books, shelf_width):

        dp = [float('inf')] * (len(books) + 1)
        dp[0] = 0

        for i in range(1, len(books)+1):
            cur_w = cur_h = 0
            j = i
            while j > 0:
                cur_w += books[j-1][0]
                if cur_w > shelf_width:
                    break
                cur_h = max(cur_h, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1]+cur_h)
                j -= 1
        
        return dp[-1]
