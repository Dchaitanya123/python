#loops in string(how to write)
name="chaitanya"
for letter in name:
    print(letter)

#loops in list 
fruits=["mango", "papaya", "orange"]
for fruits in fruits:
    print(fruits)

#loops in tuple
num=(30,87,97,86)
for num in num:
    print(num)

#loops in sets
colours={"pink","black","red","green"}
for colours in colours:
    print(colours)

#break in loops
#it exit from the loop after satisfying the condition
for i in range(1,9):
    if i==5:
       break
    print(i)

#continue in loops 
for i in range(2,35):
    if i==6:
        continue
    print(i)

#pass statements
for i in range(1,9):
    pass
print(i)

#else with loops 
#else is used for both "for" and "while" loops
for i in range(7):
    print(i)
else:
    print("not a num")

#else with break
for i in range(2,8):
    if i==3:
     break
    print(i)
else:
    print("not a num")

#using enumerate
fruits=["mango","apple", "papaya","guava"]
for index,fruits in enumerate(fruits,start=1):
    print(index,fruits)

#zip with loops 
#it gives a combined form of values in output
names=["pallavi","bhanu","sai"]
marks=[54,67,87]
for names,marks in zip(names,marks):
    print(names,marks)




