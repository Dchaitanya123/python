#all about types of arguments
#positional
#default
#keyword
#arbitory
#positional example
def greet(name,age):
    print(name)
    print(age)
greet("rahil",18)

#keyword example
def greet(sub,age):
    print(sub)
    print(age)
greet(sub="physics",age="34")

#*args
def add(*numbers):
    return sum(numbers)
result=add(20,86,75,45)
print(result)

#**kwargs
def add(*args,**kwargs):
    print(args)
    print(kwargs)
add(54,87,65,name="shyam",age=65,depth=76)
add(3,5,6,name="radha",group="mpc",age=54)

#some basic examples in variable length
def student(**kwargs):
    print(kwargs["name"])
    print(kwargs["course"])
    print(kwargs["batch"])
student(batch=3,name="karthik",course="AIRLINES")

#we can use loops in kwargs for to write our basic programes
def student(**kwargs):
    for key,value in kwargs.items():
      print(key,"i",value)
      student(name="chaitanya",age=18,section="btech")

def student(name,*marks):
    print("name:",name)
    print("*marks:",marks)
    student("chaitanya",54,76)




    
    

    