File1=open(r"C:\Users\LENOVO\Desktop\100Days\Text.txt","r")
print(File1.read())
print(File1.mode)
print(File1.name)
File1.close()
with open(r"C:\Users\LENOVO\Desktop\100Days\Text.txt","r") as file: #automatically closes the file object after running
    read=file.read()
    #read_lines=file.readline()  since you've already read the file it will return blank
    #print(read_lines) #prints blank
    print(read)
    #print(file.read(4)) prints the first 4 unread characters
print(file.closed) #shows that file is automatically closed
with open(r"C:\Users\LENOVO\Desktop\100Days\Text.txt","r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
with open(r"C:\Users\LENOVO\Desktop\100Days\text_write.txt","w") as file_write:
    file_write.write("Melina Malenia Miquella")
Lines=["Godwyn,Mohg,Morgott","Rani,Radahn,Rykard","Godfrey,Radagon"]
with open(r"C:\Users\LENOVO\Desktop\100Days\text_write.txt","w") as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
