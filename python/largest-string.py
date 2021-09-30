arr = ["sdfsdf", "sdfsdgdfgdgfgf"]

def func(arr):
    tmp = len(arr[0])
    for s in arr:
        if tmp < len(s):
            tmp = len(s)
            larg_str = s
    return larg_str

print(func(arr))
