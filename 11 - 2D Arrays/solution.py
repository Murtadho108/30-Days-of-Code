A = []

for _ in range(6):
    fill = [int(x) for x in str(input()).split(' ')]
    A.append(fill)

maximum = -9*7

for i in range(6):
    for j in range(6):
        if i+2<6 and j+2<6:
            result=A[i][j]+A[i][j+1]+A[i][j+2]+A[i+1][j+1]+A[i+2][j]+A[i+2][j+1]+A[i+2][j+2]
            if result > maximum:
                maximum=result
print(maximum)
