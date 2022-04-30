def fd(x):
    p = 0
    while True:
        if x==0:break
        p += x%2
        x //= 2
    return p

print(fd(10000000))
