'''
Author: Puffrora
Date: 2020-10-24 21:26:05
LastModifiedBy: Puffrora
LastEditTime: 2020-10-24 21:37:42
'''


"""
将问题转化为求数组和为0时的组合
 
对任何一个数，可以用三种方式对待它，乘以1，-1或0，目标是求和为0时的最大正数和
 
例如，[1，2，3], 可以对1，2乘以1，3乘以-1，此时和为0， 最大正数和为1+2=3
用字典来存储每一步的结果，键和值分别是总和以及正数和，
初始化时dp={0:0},表示和为0时的最大长度为0
那么最后只需要求dp[0]的最大值就ok辣
 
遍历所有钢筋：
对每根钢筋都有三种处理方式：加，减，丢 （对应乘以1，-1或0）
 
如：[1,2,3]
第一步: 用钢筋1，对初始的0，操作
如果加，那么总和是1，正数是1；如果减，总和是-1，正数0；如果丢，维持不变；更新dp={0:0, 1:1, -1:0}
第二步: 用钢筋2，对第一步中dp的键0，1，-1的基础上分别进行“加，减，丢 ”的操作
在0:0基础上，如果加，也就是变为2：2；如果减，变为 -2：0； 如果丢，变成0：0
类似的，在1：1基础上，加减丢变为3：3，-1：1，1：1
类似的，在-1：0基础上，加减丢变为1：2，-3：0，-1：0
每个键取较大值，用粗体标识了，然后更新dp={0:0, 1:2, 2:2, -1:1, 3:3, -2:0, -3:0}
总和为1时，相比第一步时的正数和为1，第二步时正数和变为了2，将dp[1]修改为更大的2
总和为-1时，相比第一步时的正数和为0，第二步时正数和变为了1，将dp[-1]修改为更大的1
最后返回dp[0]

https://leetcode-cn.com/problems/tallest-billboard/solution/yi-quan-ji-ben-mei-shuo-ming-bai-de-zhe-pian-kan-l/

"""
# 时间复杂度 O(N*Σ) Σ是数组所有元素和 根据题意 max(Σ) = 5000
# 空间复杂度 O(Σ)
class Solution:
    def tallestBillboard(self, rods):
        dic = {0: 0}
        for r in rods:
            # ! 用 list 否则 RuntimeError: dictionary changed size during iteration
            for k, v in list(dic.items()):
                dic[k+r] = max(dic.get(k+r, 0), v+r)
                dic[k-r] = max(dic.get(k-r, 0), v)
        
        return dic[0]
