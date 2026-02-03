#task 1
d = {"aman": 45 , "anuj": 70 , "alice": 97 ,"john": 67}
print("Enter student name:")
i = input()
print(d.get(i, "Student not found"))

#task2
a = [1,2,3,4,5,6,7,8,9,10]
print("original list ",a[0:])
print("extracted list ",a[0:5])
print("extracted reverse list ",a[4::-1])
