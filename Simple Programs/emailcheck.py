def checkemails(emails):
    try:
        username,url=emails.split('@')
        website,extension=url.split('.')
    except ValueError:
        return False
    if username.replace('-','').replace('_','').isalnum() is False:
        return False
    elif len(extension)>3:
        return False
    elif website.isalnum() is False:
        return False
    else:
        return True
def Entermail(emails):
    return list(filter(checkemails, emails))
print("Enter a value:",end="")
n=int(input())
print("Enter",n,"email adresses")
emails=[]
i=0
for i in range(n):
    emails.append(input())
Filtered=Entermail(emails)
Filtered.sort()
print("The emails are:")
print(Filtered)
