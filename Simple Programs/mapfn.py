print("Enter the number of terms:",end="")
n = int(input())
print("Enter",n,"numbers:")
arr = map(int, input().split())
arr=sorted(arr,reverse=True)
print("The array elements in reverse order:",end="")
print(arr)
for i in range(len(arr)):
    if arr[i]==arr[0]:
        continue
    else:
        print("The second largest element in the array is",arr[i])
        break
