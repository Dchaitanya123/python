#fruitful functions
#these functions are actually returns the values
#using the return keyword
#always these are important concept as useful for many purposes

#some basic operations in fruitful functions
#syntax

#def function_name(parameters)
#statments
#return type
# adding of two numbers 


def add(a,b):
    return a+b
print(add(10,67))

#squaring of two numbers
def square(x):
    return x*x
print(square(8))

#multiplying two numbers
def product(a,b):
    return a*b
print(product(76,6))

#checking even numbers
def even(n):
    return n%2==0
print(even(20))

#checking largest numbers
def largest(a,b):
    if a>b:
        return a
    else:
        return b
    print(largest(35,87))

#condition using control statements
def check(n):
    if n>0:
        return "positive"
    elif n<0:
        return "negative"
    else:
        return "zero"
    print(check(10))

#condition using loops
def total():
    s=0
    for i in range(1,6):
      s=s+i
    return s
print(total())

#excuting before statments execute
def check(n):
    if n==0:
        return "positive"
    else:
        return "negative"
print(check(0))
print(check(-34))

#when there is no return function
def display():
    print("hello world")
x=display()
print(x)

#local scope using return type
def show():
    x=10
    return x
print(show())

#global scope using return type
x=45
def show():
    return x
print(show())

#composition function using return type
def square(n):
    return n*n
def add(a,b):
    return a+b
result=add(square(3),square(4))
print(result)
    




  