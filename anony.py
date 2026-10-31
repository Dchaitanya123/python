#Anonymous Functions

#These are actually a simple type to address a functions 
#in a very simple way using lambda keyword.
#basic syntax of lambda keyword9o9o9

#"lambda arguments:expressions"

#lambda with one argument:
double=lambda x:x*2
print(double(6))

#lmabda with multiple arguments:
add=lambda a,b:a+b
print(add(10,35))

sub=lambda a,b:a-b
print(sub(45,34))

#lambda with three arguments:
add=lambda a,b,c:a+b+c
print(add(10,87,67))

#lambda argument using if, else statement:
check=lambda x:"even"if x%2==0 else "odd"
print(check(7))
print(check(6))

#lambda using with "map":
#basically map used to select all the elements in input
numbers=[1,5,7,8]
result=list(map(lambda x:x**2,numbers))
print(result)

#lambda using with "filter":
#this is opposite to map as takes only selected elements
numbers=[10,7,54,72]
result=list(filter(lambda x:x%2==0,numbers))
print(result)

#lambda using "sorting":
#lambda is actually used for this sorting for giving
#particular value.
student=[
    ("Ravi",45),
    ("Meena",54),
    ("karthik",87)
]
result=sorted(student,key=lambda x:x[1])
print(result)

#checking maximum or not
check=lambda a,b:a if a>b else b
print(check(43,87))

#function with return type
def add(a,b):
    return a+b
print(add(45,54))
c=add(45,54)
def sub(a,b):
    return a-b
print(sub(56,45))
d=sub(56,45)
print(c*d)


