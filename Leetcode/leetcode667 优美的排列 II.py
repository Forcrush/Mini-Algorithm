'''
Author: Puffrora
Date: 2020-10-21 09:49:26
LastModifiedBy: Puffrora
LastEditTime: 2020-10-21 10:08:30
'''


"""
当 k=n-1 时，有效的构造是 [1, n, 2, n-1, 3, n-2, ....]。我们需要 n-1 个的不同的相邻整数差，
这意味着我们需要 1 和 n 相邻；然后，我们需要 n-2 的差异以此类推

另外，k=1 时，有效的构造是 [1, 2, 3, ..., n]。所以我们有一个构造，我们可以将 k=n-1 和 k=1 
的构造方法结合起来。我们可以先构造 k=1 的序列 [1，2，…，n-k-1]，这样剩下需要构造的序列的长度
 n 实际上就是 k+1，然后用 k=n-1方法完成构造。

例如，当 n=6 和 k=3 时，我们将数组构造为 [1, 2, 3, 6, 4, 5]。这包括两部分：
构造 [1，2] 和构造 [1，4，2，3]，其中每个元素都添加了 2（即 [3，6，4，5]）

算法：
和上面说的一样，先构造 [1，2，…，n-k-1]。剩下的 k+1 个元素是[n-k，n-k+1，…，n]，我们将按头尾顺序交替写入。

https://leetcode-cn.com/problems/beautiful-arrangement-ii/solution/you-mei-de-pai-lie-ii-by-leetcode/
"""
class Solution:
    def constructArray(self, n, k):

        arr = [i+1 for i in range(n)]

        p1 = arr[:n-k-1]
        p2 = arr[n-k-1:]

        def interchange(a):
            left, right = 0, len(a) - 1
            tmp = []
            operation = 1
            while left <= right:
                if operation == 1:
                    tmp.append(a[left])
                    left += 1
                    operation *= -1
                elif operation == -1:
                    tmp.append(a[right])
                    right -= 1
                    operation *= -1
            return tmp
        
        return p1 + interchange(p2)
                
        