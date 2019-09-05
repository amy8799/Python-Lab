students={'1MS17IS021':'Amy','1MS17IS022':'Ana','1MS17IS099':'Suma','1MS17IS028':'Ken'}
list=["value1","value 2","value 3","value 4"]
list2=[]
j=0
for i in students:
    print("Key is",i,"\t value is",students[i])
    list[j]=students[i]
    j=j+1
print(list)
print(students.keys())
print(students.values())
print(students.items())