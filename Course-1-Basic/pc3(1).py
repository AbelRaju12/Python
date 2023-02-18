import matplotlib.pyplot as plt
#%matplotlib inline
#functions is apiece of code that you can reuse
l=len([1,2,3,4]) #here len is an inbuilt function
s=sum([1,2,3,4])
x=[1,3,6,3,6,7,8,6,2]
x_sorted=sorted(x) #here simply using sorted doesn't change 'x'

def plus(a):

    """
     Adds 1
    """
    b=a+1 #the above is the documentation for the function
    return b
a=5                                             # enumerate is used print indexes along woth list values
c=plus(a)
help(plus) #shows the documentation
print(a,c)
 # mult(2,"a string") which is amultiplication string just repeats the string twice here
def nope():
     pass #for an empty fn
def Print(A):
    for a in A:
        print(a+'1')
Print(['a','b','c'])
def isGoodRating(rating=4):
    if(rating < 7):
        print("this album sucks it's rating is",rating)

    else:
        print("this album is good its rating is",rating)
isGoodRating()
isGoodRating(10)
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")

class Rectangle(object):

    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height
        self.width = width
        self.color = color

    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()

R1=Rectangle(3,6,'r')
R1.drawRectangle()
