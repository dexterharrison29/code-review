def value(r):
    sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = 0
    for idx, val in enumerate(r):
        first_num = num[sym.index(val)]
        second_num = num[sym.index(r[idx + 1])] if idx + 1 != len(r) else -1
        if first_num >= second_num:
            result += first_num
        else:
            result -= first_num
    return result
