#dictionary 
#unordered,mutable and main thing key values pairs

student={'name':'chaitu' ,'age':18 ,'sub':'python' ,'course':'aiml' ,'city': 'bangalore'}
print(student.keys())
print(student.values())
print(student.items())

#acess the  elements in a dictionary
print(student['name'])
print(student['age'])
print(student['course'])

#changes all the values in dic
student["age"]=18
print(student["age"])

#add new data in a dic
student['grade']= 'A'
print(student['grade'])

#remove the data
student.pop('city')
print(student)

#get method in dic
print(student.get('name'))

#update method in dic
student.update({'age':19})

#setdefault method in dictionary
student.setdefault('gender','female')

#pop item method in dictionary
print(student)

#clear method
student.clear()
print(student)

#copy method
student={"name":"bunny" , "age":18}
new_student=student.copy()
print(new_student)

#BODMAS(order of evaluation)
res=2+13*2
print(res)