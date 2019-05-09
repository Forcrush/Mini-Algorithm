def convert(s, numRows):
    if s == '' or numRows == 1:
        return s
    r = int(len(s) / (2 * numRows - 2))
    res = ''
    for i in range(0, numRows):
        for c in range(0, r + 1):
            if i == 0:
                if c * (2 * numRows - 2) > len(s) - 1:
                    res += ''
                else:
                    res += s[c * (2 * numRows - 2)]
            elif i != numRows - 1:
                if i + c * (2 * numRows - 2) > len(s) - 1:
                    res += ''
                else:
                    res += s[i + c * (2 * numRows - 2)]
                if (2 * numRows - 2 - i) + c * (2 * numRows - 2)  > len(s) - 1:
                    res += ''
                else:
                    res += s[(2 * numRows - 2 - i) + c * (2 * numRows - 2) ]
            else:
                if numRows - 1 + c * (2 * numRows - 2) > len(s) - 1:
                    res += ''
                else:
                    res += s[numRows - 1 + c * (2 * numRows - 2)]
    return res

print(convert("LEETCODEISHIRING", 4))