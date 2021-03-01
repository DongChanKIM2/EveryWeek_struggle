arr = list(input())
print(arr)
result = []
for i in range(len(arr)):
    result.append(arr[i])
    if arr[i] == ')' and result[-2] == '(':
        result.pop()
        result.pop()

print(result)
