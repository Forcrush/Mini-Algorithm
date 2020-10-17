'''
Author: Puffrora
Date: 2020-10-16 15:49:06
LastModifiedBy: Puffrora
LastEditTime: 2020-10-16 15:59:30
'''


# 贪心算法
# 时间复杂度 O(N)
# 空间复杂度 O(N)
class Solution:
    def minSwapsCouples(self, row):

        def get_lover_id(cur_id):
            return cur_id - 1 if cur_id % 2 else cur_id + 1
        
        pos_dic = {v: i for i, v in enumerate(row)}
        change_time = 0

        for i in range(0, len(row), 2):
            cur_id = row[i]
            lover_id = get_lover_id(cur_id)
            if row[i+1] != lover_id:
                lover_pos = pos_dic[lover_id]
                row[i+1], row[lover_pos] = row[lover_pos], row[i+1]
                pos_dic[lover_id] = i + 1
                pos_dic[row[lover_pos]] = lover_pos
                change_time += 1
        
        return change_time

 
