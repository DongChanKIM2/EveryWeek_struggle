def dc(n, m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    elif m % 2 == 0:
        return dc(n, m//2) * dc(n, m//2)
    elif m % 2:
        return dc(n, m//2) * dc(n, m//2) * n


n, m = map(int, input().split())
print(dc(n, m))