#question on slicing

#take input and print middle 3 characters , last 2 character
str= input("Enter the Value : ")
mid= len(str)//2
output1= str[mid-1:mid+2]
output2= str[len(str)-2: ]
print("the middle three characters :",output1)
print("the last two characters :",output2)
