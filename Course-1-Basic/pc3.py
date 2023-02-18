#COmparison operators
a=6
print(a==7,"Abel"=="Pegasus") # < > !=
print('BA' > 'AB') #result based on ASCII values
#Branching
if (a>5):
    print("yeah genius..!")
elif (a<5):
    print("Nope..")
else:
    print("How in the goddaam....!!")
#you can use 'or' 'and' to join two conditions
#Loops
for i in range(0,5):  #from 0 to 4 auto increment
    print(i)
squares=[0,1,4,9,16]
for square in squares:
    print(square)
for i,x in enumerate(squares): #prints index in i and values in x
    print(i,x)
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[0]
while(i < len(PlayListRatings) and rating >= 6):
    print(rating)
    i = i + 1
    rating = PlayListRatings[i]
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)
