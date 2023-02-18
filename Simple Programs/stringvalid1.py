def printt(t):
    if t==1:
        print(True)
    else:
        print(False)
s = input()
t=0
for i in s:
    if i.isalnum()==True:
        t=1
        break
printt(t)
t=0
for i in s:
    if i.isalpha()==True:
        t=1
        break
printt(t)
t=0
for i in s:
    if i.isdigit()==True:
        t=1
        break
printt(t)
t=0
for i in s:
    if i.islower()==True:
        t=1
        break
printt(t)
t=0
for i in s:
    if i.isupper()==True:
        t=1
        break
printt(t)
