# 0 1 1 2 3 5 8 ...

a, b = 0, 1
num = 30
while a < num:
    print(a)
    a, b = b, a+b
