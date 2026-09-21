# Dictionary basics

student= {
    "name": "Vansh Mani",
    "City": "Garhwa",
    "Age": 20,
    "rollNumber": 3391
    
}
print(type(student))
print(student["name"])
print(student["City"])
student["City"]= "Bhubaneshwar" 
student["favSubject"]= "MATHS"
student.pop("City")
print(student)
print(student.keys())
print(student.values())
print(student.items()) # .clear kabhi use nahi karna nahi to gaze ho jayega


