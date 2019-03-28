N = int(input())
result = 0
maximum = 0

while N>0:
    if N%2 == 1:
        result = result+1
        if result>maximum:
            maximum = result
    else:
        result = 0
    N = N//2
print(maximum)
