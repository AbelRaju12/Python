import sys
print(sys.version) #prints the Python version
print(sys.int_info)
print(int(3.5))
print(bool(0))
print(int(False))
print(27//7)
Y="Marika the Eternal"
Z=Y[::2] #selects every second character
X=Y[2:8:3] #selects every second character between 2nd and 8th characters
print(Z, X)
print(Y[-4]) #you can use negative numbering as well where the last character is -1 and decreases backwards on the string
x=Y.find('Marika')#prints the position of the first letter of the desired word else prints -1
y=Y.replace("Marika","Queen Marika")
print(x, y)
str1=str(1+1) #here argument is evaluated first
str2=str("1+1")
print(str1,str2)

#WEEK 1 is completed
