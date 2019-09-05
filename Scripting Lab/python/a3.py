#Dictionary that holds details of students and printing details of students with even register numbers 
Student={
    21:{
        "name":'Amy',
        "age":20,
        "section":'A'
    },
    36:{
        "name":'Annie',
        "age":20,
        "section":'A'
    },
    42:{
        "name":'Harini',
        "age":20,
        "section":'A'
    },
    108:{
        "name":'Swara',
        "age":20,
        "section":''
    }
}
print("Details of students with even register numbers")
for i in Student:
        if i%2==0:
           print(Student[i])
