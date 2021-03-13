def find_max(l):
    max = l[0]
    for num in l:
        if num > max:
            max = num
    return max