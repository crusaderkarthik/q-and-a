## Write a program to find 2 maximum value of input 3 numbers
x=int(input())
for i in range(x):
    y=list(map(int,input().split()))
    y.sort()
    print("The maximum 2 numbers in the given 3 numbers are ", (y[1],y[2]))
    
