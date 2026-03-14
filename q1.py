n = int(input())
arr = list(map(int, input().split()))

sum_val = 0

for i in range(n):
    sum_val = sum_val + arr[i]

print(sum_val)
