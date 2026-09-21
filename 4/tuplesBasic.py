tup = (1,2,3,4,5)
print(tup[0]) #1

# tuple basics

myTuple= (78,90,75)
studentTuple= ("Khushi", "Divya", "Ishaan")

#studentTuple[1]= "Aanchal" Tuple are immutable/Not changeable
print(studentTuple[2]) # Ishaan

#EMPTY TUPLES

emptyTuple= ()
singleTuple= (1)
print(type(singleTuple)) # class integer
print(type(emptyTuple)) #class tuple
print(type(studentTuple)) #class tuple
print(studentTuple.index("Ishaan")) #2
print(studentTuple.count("Divya")) #1
print(len(studentTuple)) #3