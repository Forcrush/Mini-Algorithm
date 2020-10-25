'''
Author: Puffrora
Date: 2020-10-25 21:04:01
LastModifiedBy: Puffrora
LastEditTime: 2020-10-25 22:43:03
'''


"""
可以先求由各个位不重复数组成的数字个数，令 N 的位数为 k
第一种情况求位数小于k的不重复数字的个数：
因为最高位总是为0，因此一开始剩下的数字 j 总是为9个（1-9），然后剩下的低位可选的数字总共有 A(10-1,i)

第二种情况求位数为k的不重复数字的个数：
一开始剩下的数字 j 受数字 N 每位上的数字影响，设 N 的当前位的数字为 n，则 j<=n，然后剩下的低位可选的数字总共有 A(10-(k-i),i)

我们具体来看一个例子，比如3562这个数字

对于第一种情况，将其排列组合可以选择的数字列出来
4th 3th 2th 1th total
 0   0   0  1-9 9xA(9,0)
 0   0  1-9 0-9 9xA(9,1)
 0  1-9 0-9 0-9 9xA(9,2)

对于第二种情况：
4th 3th 2th 1th total
1-2 0-9 0-9 0-9 2xA(9,3)
 3  0-4 0-9 0-9 5xA(8,2)
 3   5  0-5 0-9 6xA(7,1)
 3   5   6  0-1 2xA(6,0)
 3   5   6   2  1

注：total为理想的总数，最后还需要将重复的数字剔除，
比如第二种情况的第二行中，如果遍历到了33xx，则后面的xx不需要再计算，因为高位的33已经使这个数字变为了重复数字，循环可以直接break掉

https://leetcode-cn.com/problems/numbers-with-repeated-digits/solution/zui-kuai-zui-qing-xi-de-jie-fa-by-woodnote/

"""
class Solution:
    def numDupDigitsAtMostN(self, N):

        def factor(n):
            if n == 0: return 1
            return n * factor(n - 1)

        def A(m, n):
            if n == 0: return 1
            return factor(m) // factor(m-n)

        def find_no_dup(N):
            digit = len(str(N))

            # 第一种情况
            sum1 = 0
            for i in range(1, digit):
                sum1 += 9 * A(9, i-1)
            
            # 第二种情况
            sum2 = 0
            have_dup = False
            num = [int(i) for i in str(N)]
            num_have = {}
            for k in range(len(num)):
                # 检查 N 这个数字前 k 位是否有重复 若有直接中断循环
                if have_dup: break
                num_have[num[k]] = num_have.get(num[k], 0) + 1
                if num_have[num[k]] > 1: have_dup = True
                for cur in range(1 if k == 0 else 0, num[k]):
                    if cur not in num_have:
                        sum2 += A(10-(k+1), digit-(k+1))
            
            # 判断这个数自身是否满足不重复
            sum2 += (len(set(num)) == len(num))
            
            return sum1 + sum2
        
        return N - find_no_dup(N)

print(Solution().numDupDigitsAtMostN(111))
