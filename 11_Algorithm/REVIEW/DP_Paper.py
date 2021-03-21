def dp(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    elif n >= 2:
        return dp(n-1) + (2*dp(n-2))


t = int(input())
for tc in range(t):
    n = int(input())
    n //= 10
    print('#{}'.format(tc+1), end=' ')
    print(dp(n))
    # print('{}'.format(print(dp(n))))
