#scope and global functions
#there are actually two types in scope variable
#local variables and global variables

#local variables
#these functions are actually accessed inside the function
#within the function only
def display():     #----------1
    name="chaitu"
    age=23
    print(name)
    print(age)
display()

def student():      #----------2
    x=245
    print(x)
student()

def student():      #-----------3
    num=[45,76,56]
    print(num)
student()

def add(a,b):       #----------4
    return a+b
print(add(43,87))

#global variables
#these functions are actually accessed outside the function
#within that outside and inside function only

x=26
def display():
    print(x)
display()

x=245
def display():
    y=456
    print("global  first number",x)
    print("global second number",y)
display()

x=67
def display():
    x=45
print("inside function",x)
display()
print("outside function",x)






