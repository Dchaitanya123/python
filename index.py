#comparison operator
a=10
b=20
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

age=int(input("Enter your age:"))
print("Eligible:", age>=18)

marks=int(input("Enter your marks:"))
print("passed:", marks>=45)

correct_username="admin"
correct_password="3456"
username=input("Enter your username:")
password=input("Enter your password:")
print(username == correct_username)
print(password == correct_password)

age = 45
citizen = True
print( age>18 and citizen == True)

tarun = True
pardu = False
print(tarun or pardu)

karthik = False
print(not karthik)

marks = float(input("Enter your marks:"))
attendence = float(input("Enter your attendence:"))
eligible = marks>=56 and attendence>=76
print("scholarship eligible:" , eligible)

a=5
b=3
print(a>>b)

units=int(input("Electricity units:"))
rate=6
bill=rate*units
print("Electricity bill:",bill)

travel=float(input("travel expence:"))
food=float(input("food expence:"))
hotel=float(input("hotel expence:"))
total=travel+food+hotel
print("total expence:,total")