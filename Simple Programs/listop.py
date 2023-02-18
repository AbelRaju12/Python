print("Enter a value:")
n=int(input())
print("Enter a command and value:")
list=[]
for i in range(n):
    list.append(input().split())
listf=[]
for i in range(n):
    if list[i][0]=='insert':
        listf.insert(int(list[i][1]),int(list[i][2]))
    elif list[i][0]=='append':
        listf.append(int(list[i][1]))
    elif list[i][0]=='remove':
        listf.remove(int(list[i][1]))
    elif list[i][0]=='pop':
        listf.pop()
    elif list[i][0]=='sort':
        listf.sort()
    elif list[i][0]=='reverse':
        listf.reverse()
    elif list[i][0]=='print':
        print(listf)
