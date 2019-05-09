def myAtoi(str):
    if str == '':
        return 0
    num = ['0','1','2','3','4','5','6','7','8','9']
    flag = ['-','+']
    numflag = False
    res = ''
    resflag = '+'
    for i in range(0, len(str)):
        if numflag == True and str[i] not in num:
            break
        if str[i] == ' ':
            continue
        if str[i] in num:
            res += str[i]
            numflag = True
            continue
        if str[i] in flag and i != len(str)-1 and str[i+1] not in num:
            break
        if str[i] in flag and numflag == False:
            resflag = str[i]
            continue
        break
        
    if res == '':
        return 0
    elif resflag == '+':
        if int(res) > 2**31 - 1:
            return 2**31 -1
        else:
            return int(res)
    else:
        if -1 * int(res) < 2**31 * -1:
            return 2**31 * -1
        else:
            return -1 * int(res)