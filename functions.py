#functions
#basic function
def greet():
    print("hello")
    print("welcome to python")
greet()

#functions without parameters
def welcome():
    print("welcome to python")
welcome()
welcome()
welcome()

#function with parameters
def greet(name):
    print("hello",name)
greet("chaitu")
greet("jyothika")

#add two numbers(multiple parameters)
def greet(a,b):
    print("sum",a+b)
greet(20,35)
greet(10,84)

#function with return value
def add(a,b):
    return a+b
result=add(10,20)
print(result)

#function with even and odd
def check_even_odd(number):
    if number%2==0:
       return "Even"
    else:
        return"odd"
result=check_even_odd(35)
print(result)

#functions for largest of two numbers
def check_largest(a,b):
    if a>b:
        return "a"
    else:
        return "b"
result=check_largest(20,50)
print(result)

#functions with largest of three numbers
def check_largest(a,b,c):
    if a>b:
        return "a"
    else:
        return "b"
    if b>c:
        return "b"
    else:
        return "c"
    if c>a:
        return "c"
    else:
        return "a"
result=check_largest(20,74,34)
print(result)

#function + user input       -------------1
def square(number):
    return number*number
number=int(input("Enter a number:"))
result=square(number)
print("square",result)

#sum of two number taking user inputs
def add(x,y):
    return x+y
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
result=add(x,y)
print("sum=",result)
    
#even or odd user input
def check_even_odd(x):
    if x%2==0:
        return "Even"
    else:
        return "odd"
x=int(input("Enter a number:"))
result=check_even_odd(x)
print(result)

#largest of three numbers taking user
def check_largest(x,y,z):
     if x>y:
        return "x"
     else:
        return "y"
     if y>z:
        return "z"
     else:
         return "y"
     if z>x:
         return "z"
     else:
         return "x"

x=int(input("Enter a number"))
y=int(input("Enter a number"))
z=int(input("Enter a number"))
result=check_largest(x,y,z)
print("result",check_largest)

#grade calculation
def find_grade(marks):
    if marks >=90:
        return "A"
    elif marks>=80:
        return "B"
    elif marks>=70:
        return "C"
    else:
        return("fail")
m=int(input("Enter a number:"))
print("grade:",find_grade(m))

#temperature check
def check_temperature(degree):
     if degree>70:
         return "high temperature"
     elif degree>40:
         return "low temperature"
n=int(input("Enter a number:"))
print("temperature",check_temperature(n))

# functions with loops 
def multiplication_table(num):
    for i in range(1,11):
     print(num,"*",i,"=+,num*i")
    i+=1
    return num*i
num=int(input("Enter number:"))
result=multiplication_table(num)
print(result)


#functions with sum of 1 to n
def sum_n(num):
    total=0
    for i in range(1,num+1):
        total+= i
    return total
n=int(input("Enter n:"))
print("sum=",sum_n)


#function with factorial
def factorial(n):
     result=i
     for i in range(1,n+1):
       result*=i
       return result
n=int(input("Ent=er a number:"))
print("factorial:",factorial(n))

#sum of digits
def sum_digits(n):
    total=0
    while n>0:
        digits=n%10
        total+=digits
        n//=10
    return total
num=int(input("Enter a number:"))
print("sum of digits =",sum_digits(num))

#pallindrome check
def is_pallindrome(n):
    original=n
    reverse=0
    while n>0:
        digits =n%0
        reverse=reverse*10+digits
        n//=10
    if original==reverse:
        return True
    else:
        return False
    num=int(input("Enter a number"))
    if is_pallindrome(num):
        print("pallin drome")
    else:
        print("not pallindrome")

#default functions --------------------------7/10/26
#it is actually a type in user defined function
def add(a=24,b=56):
    print(a+b)
add()

#ordered parametric functions
#if we exchange the variable names also it will give in a order 
#way
def add(b,a):
    print(a)
    print(b)
add(10,20)

#keyword argument parametric function
def add(a,b):
    print(a)
    print(b)
add(a=4,b=5)

#variable length parametric function
def add(*a):
    print(sum(a))
add(19,65,46)

    

    


