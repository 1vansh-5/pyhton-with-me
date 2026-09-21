# You are given a list of programming languages:
# ["Python", "Java", "C","Python", "Java", "C"]
# Convert it into a set and print how many unique languages Divya knows

programmingList= ["Python", "Java", "C++","Python", "Java", "C++","C"]
print(type(programmingList))
# How to convert a list into set

programmingSet= set(programmingList)
print(programmingSet)

print(type(programmingSet))
print("Divya knows these many languages", len(programmingSet))