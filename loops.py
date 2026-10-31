           #loops
#these are used to execute block of codes
#for loop
#it is used to execute the code repeatedly in a sequence way.
for i in range(1,8):
    print(i)

#even numbers
for i in range(0,51,2):
    print(i)

#odd numbers
for i in range(1,51,2):
    print(i)

for i in range(10,1,-1):
    print(i)

#even num and odd num
for i in range(2,51,2):
    print(i)
for i in range(1,51,2):
    print(i)

#multiple of 5 to 50
for  i in range(0,55,5):
    print(i)

#multiplication of table
num=int(input("Enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#sum of num from 1 to n
n=int(input("Enter a number"))
total=0
for i in range(1,n+1):
    total=total+i
    print("sum:",total)

#factorial of numbers
n=int(input("Enter a number:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
    print("factorial:",factorial)

#sum of even no. 2 to n
n=int(input("Enter a number:"))
total=2
for i in range(2,n+1,2):
    total=total+2
    print("sum:",total)

#count of multiples of 3
n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if i % 3==0:
        count=count+1
        print("count:",count)

#sum of multiples of 5
n=int(input("Enter a number:"))
total=0
for i in range(1,n+1):
    if i ==0:
        total=total+i
print("sum:",total)

#even numbers/odd numbers fronm 2 to 50 using while
i=2
while i<=50:
    print(i)
    i=i+2


i=1
while i<=50:
    print(i)
    i=i+1

#print  all the no. until it comes 0
total=0
num=int(input("Enter a num:"))
while num!=0:
    total=total+num
    num=int(input("Enter num:"))
    print("total:",total)


#count the number of digits in a number ---.
number=int(input("Enter number:"))
count=0
while number>0:
    number=number//10
    count=count+1
    print("number of digits:",count)

#sum of the digits in a number
number=int(input("Enter number:"))
total=0
while number>0:
    digits=number%10
    number=number//10
    total=total+digits
    print("sum of digits:",total)

#reverse a number
number=int(input("Enter a number:"))
total=0
while number>0:
    digits=number%10
    number=number//10
    total=total+digits
    print("si=um of digits:",total)

#check if it is a pallandrome
number=int(input("Enter a number:"))
original=number
reverse=0
while number>0:
    digits=number%10
    reverse=reverse*10+digits
    number=number//10
if original==reverse:
    print("pallindrome")
else:
    print("not a pallindrome")


# check if a a num is prime ...................!
num=int(input("Enter a num:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
    if count==2:
        print("prime number")
    else:
        print("not a prime number")

#print all the prime num between 2 to 100
for num in range(2,100):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
        if count==2:
            print(num)


#break 
for i in range(1,9):
     if i==6:
      break
print(i)

#continue
for i in range(1,15):
    if i==8:
        continue
    print(i)

for i in range( 1,11):
    if i%2==0:
        continue
    print(i)

#print num until user enter 0
while True:
    num=int(input("enter a num:"))
    if num==0:
        break
    print("you entered:",number)

#print num 1 to 100 but skip multiple of 3 and stop at 50
for i in range(1,101):
    if i==50:
       break
    if i%3==0:
        continue
    print(i)


#calculate the sum of positive numbers entered by thr user
while True:
    number=int(input("Enter number:"))
    if number<0:
       continue
    if number==0:
        break
    total=total+number
    print("total:",total)

#find the first number between 1 and 100 that is divisible by by 3 and 5
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("first number,i")
        break

#sum calculations
total=0
for i in range(10):
    number=int(input("Enter a number:"))
    if number <0:
        continue

total=total+number

#find the largest number among 5 numbers entered by the user
largest=None
for i in range(5):
    number =int(input)("Enter the number:")
    if largest is none or number>largest:
        largest=number
        print("largest:",largest)

# for smallest no.
    for i in range(5):
        number =int(input)("Enter the number:")
    if largest is none or number<largest:
        largest=number
        print("largest:",largest)    


