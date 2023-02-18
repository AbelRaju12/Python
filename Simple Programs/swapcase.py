def swapcase(s):
    swapping=[]
    for i in range(len(s)):
        if s[i].isupper()==True:
            swapping.append(s[i].lower())
        elif s[i].islower()==True:
            swapping.append(s[i].upper())
        else:
            swapping.append(s[i])
    swapped=''
    return(swapped.join(swapping))
    
print("Enter the string: ",end="")
string=input()
string_swapped=swapcase(string)
print("The case swapped string is:",string_swapped)
