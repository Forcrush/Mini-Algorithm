'''
Author: Puffrora
Date: 2020-10-17 21:59:34
LastModifiedBy: Puffrora
LastEditTime: 2020-10-17 22:43:13
'''

"""
set(). remove() vs discard() vs pop()
If you are sure that element to be deleted exists in the set then use the remove() function to delete that element. It is fast because it does not check if the given element exists in the set or not. But it will throw a KeyError in case the element does not exist in the set.
If you are not sure that element to be deleted exists in the set or not, then use the discard() function to delete that element. It will not throw any error, if the given element does not exist in the set.
If you want to delete a random element from a set and also want to know what is deleted. Then use the pop() function.
"""
class Solution:
    def isNStraightHand(self, hand, W):
        
        if len(hand) % W: return False

        dic = {}
        for i in hand:
            dic[i] = dic.get(i, 0) + 1
        
        for _ in range(len(hand)//W):
            first = min(dic)
            for i in range(W):
                if first + i not in dic:
                    return False
                dic[first+i] -= 1
                if dic[first+i] == 0:
                    del dic[first+i]
        
        return True
