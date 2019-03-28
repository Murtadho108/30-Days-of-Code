# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for i in range(n):

    string = input()

    for j in range(len(string)):
        if j % 2 == 0:
            print(string[j], end='')

    print(" ", end='')

    for j in range(len(string)):
        if j % 2 != 0:
            print(string[j], end='')

    print("")
