n=int(input())
i=0
for i in range(n):
    print("The number is",int(i))
    i=i+1
i=0
while i<n:
    print("The square of",i,"is:",int(i*i))
    i=i+1
i=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print(" ")
