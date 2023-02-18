Tuples=(1,2,4,8,9) #tuples are collection of elements
Tuples2=(1,"Abel",23.78) #can contain different elements but its type will be tuple
print(type(Tuples2))
print(type(Tuples2[-1])) #indexing same as strings
print(len(Tuples))
#Tuples are immmutable. If you want to manipulate a tuple create another. You can nest tuples.
NT=(1,(3,4),2)
print(NT[1])
print(NT[1][0]) #prints 0th element of the tuple in 1st position

#Lists are similar to tuples but are mutable. They represented using []
Lists=[1,[2,3,4,'A'],5,6,('Pega','sus')] #nesting is aok
print(Lists)
Lists.extend(["pop",6]) #muting. appends adds one more element. or simply list[0]=5
print(Lists)
str="I am the legend"
str1=str.split() #converts string to lists with blank spaces or use __.split(",")
print(str1[3])
#there is also lists aliasing, to fight use A=B[:]
# help(Lists)
#Dictionaries are set o keys and values
D={1:'a',2:'A',3:'b'} #keys are immutable and values are mutuable
print(D[2]) #acces values using keys
print(3 in D) #check key presence
#use    ___.values() and    ___.keys()
# Sets are collection of elements with no imp for positon and no duplicates
#convert lists and tuples =set()
sets={"A","B","C"}
sets.add("D")
sets.remove("B")
print(sets) # can use 'in' fn
# set= set1 & set2
# set=set1.union(set2)
# set1.issubset(set2)
# album_set1.difference(album_set2)
# album_set1.intersection(album_set2)   
