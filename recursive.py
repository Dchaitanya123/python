#Recursion 
#it is a kind of a topic where a function calls itself again and again repeatedly
#in the body until the condition satisfied
#syntax 
#def function_name():
#if condition:
#return
#else:
#function_name()

#simple program using recursion
def display(n):
    if n==5:
        return
    print(n)
    display(n+1)
display(1)

#factorial program----------important
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#user giving input example
def sum_n(n):
    if n ==0:
        return 0
    else:
        return n+sum_n(n-1)
n=int(input("Enter a number:"))
result=sum_n(n)
print("sum of",n,"number is:",result)

#four types of recursive 
#direct recursive
#it calls function directly
def display(n):
    if n==0:
        return
    print(n)
    display(n-1)
display(3)


#indirect type of recursive
#it contain one function in which this function calls the second function again 
def function1(n):
    if n>0:
       print(n)
       function2(n-1)
def function2(n):
    if n>0:
        print(n)
        function1(n-1)
function1(3)

#tail recuesion
#it actually use for those programs when the calling done in recursive with only last operation

#sum of natural numbers
def sum(n):
    if n==0:
       return 0
    else:
       return n+sum(n-1)
print(sum(6))

#fibonacci series
#getting a partcular number by adding the previous and that previous numbers.
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(5):
    print(fibonacci(i),end="")


#reversing the number with user defined
def number(n,result=0):
    if n==0:
        return result
    else:
        return number(n//10,result*10+n%10)
print(number(5678))

# finding power of number
def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
print(power(2,4))



       


           
    


