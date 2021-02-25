'''
Author: Puffrora
Date: 2021-02-25 21:55:11
LastModifiedBy: Puffrora
LastEditTime: 2021-02-25 22:24:51
'''


# 回溯法 取模
# 通过求解父点完成 (x, y) -> (x-y, y) 或 (x, y-x)
# 时间复杂度 O(log(max(tx, ty)))
# 空间复杂度 O(1)
class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        
        while tx >= sx and ty >= sy:
            # 除非 sx=sy=tx=ty=0 否则不存在
            if tx == ty: break

            # 父节点为(x-y, y)
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                # 此时 ty=sy ty不再改变
                else:
                    return (tx - sx) % ty == 0
            
            # 父节点为(x, y-x)
            else:
                if tx > sx:
                    ty %= tx
                # 此时 tx=sx tx不再改变
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy

