print("Enter the number of students:",end="")
n=int(input())
student_marks={}
print("Enter",n,"student_name and marks of three subjects:")
for i in range(n):
    line=input().split()
    name,score=line[0],line[1:]
    score=map(float,score)
    student_marks[name]=score
print("Enter the student name:",end="")
name_=input()
marks=0
for i in student_marks[name_]:
    marks=marks+i
avg=float(marks/3)
print("The average mark for",name_,"is",avg)
