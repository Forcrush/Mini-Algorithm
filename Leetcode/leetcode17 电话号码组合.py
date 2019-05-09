class Solution:
    def __init__(self):
        self.res = []
    def all_com(self, l):
        path = ''
        flag = True
        for i in range(len(l)):
            if len(l[i]) == 1:
                path += l[i]
            else:
                tmp1 = l[:i]
                tmp1.append(l[i][0])
                tmp1.extend(l[i+1:])
                self.all_com(tmp1)

                tmp2 = l[:i]
                tmp2.append(l[i][1:])
                tmp2.extend(l[i+1:])
                self.all_com(tmp2)

                flag = False
        if flag:
            self.res.append(path)
            
    def letterCombinations(self, digits):
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if digits == '':
            return []
        inp = []
        for i in digits:
            inp.append(dic[i])
        self.all_com(inp)
        return list(set(self.res))
