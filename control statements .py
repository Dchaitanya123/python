#if statements
#it happens when condition is true only
#age                              ---- 1
age=int(input("Enter you are age:"))
if age>=24:
   print("Eligible")

#marks                             --- 2
marks=int(input("Enter your marks:"))
if marks>=90:
   print("pass the exam:")
else:
   print("not upto mark:")

#purchasing
price=int(input("Enter the price pf mangoes:"))
if price>=560:
   print("purchase:")
else:
   print("not purchase:")

#elif statement                     ----- 3
marks=78
if marks>=90:
   print("grede A:")
elif marks>70:
     print("grade B:")
else:
     print("grade C:")

#nested if condition
#"nested if" in the sence it has another if statement
#under  if statement.
age=18                           ----- 4
has_id=True
if age>=18:
   print("You are an adult:")
if has_id:
   print("you can enter:")

   #PROBLEMS
   number=int(input("Enter a number:"))
   if number%5==0:
      print("divisible by 5:")

    #Temperature check
temperature=float(input("Enter the temperature:"))
if temperature>50:
      print("High temperature:")

  #even and odd                
a=int(input("Enter a number:"))
if   a%2==0:
     print("Even number:")
else:
     print("odd number:")

#pass or fail
d=int(input("Enter a number:"))
if d>=100:
   print("PASS:")
else:
    print("FAIL:")

#greater then number
number=int(input("Enter a number"))
if number>100:
   print("number is greater then 100:")
else:
   print("number is not greater then 100:")

   #operators
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
operator=input("Enter operator (+,-,*,/):")
if operator=="+":
    print("result:",a+b)
elif operator=="-":
    print("result:",a-b)
elif operator=="*":
    print("result:",a*b)
elif operator=="/":
    if b!=0:
       print("result:",a/b)
    else:
       print("cannot divide by zero")
else:
       print("invalid operator")

   #marks and attendence
marks=int(input("Enter your marks:"))
attendence=int(input("Enter your attendence:"))
if marks>75 and attendence>40:
   print("eligible:")
else:
   print("not eligible:")

  #check balance
balance=(float(inout("Enter balance:")))
amount=float(input("Enter withdrawl amount:"))
if amount>0:
   if amount<=balance:
        balance=balance-withdraw
        print("Withdrawl successful:")
        print("Remaining balance:")
else:
      print("Insufficient balance")
   else:
    print("invalid amount:")