def stringmut(string,position,char):
    l=list(string)
    l[position]=char
    return ''.join(l)
print("Enter the string: ",end="")
s=input()
print("Enter the new character and its postion: ",end="")
c, p=input().split()
s_mutated=stringmut(s,int(p),c)
print("The new string is:",s_mutated)
