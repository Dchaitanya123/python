marks=[60,98,76,54]
print(marks)

marks=[54,98,76,64,53]
print(marks[0])
print(marks[2])
print(marks[3])

#change elements in a lists
marks=[45,87,67]
marks[2]=54
print(marks)

#add elements to alist
marks=[65,97,84]
marks.append(87)
print(marks)

#remove elements
marks=[45,76,86,98]
marks.remove(76)
print(marks)

#insert elements
marks=[45,76,98]
marks.insert(2,76)
print(marks)

#extend elements
a=[43,76,98]
b=[54,87,54]
a.extend(b)
print(a)

#clear elements
a=[3,5,7]
a.clear()
print(a)

#index of elements
d=[6,7,8,9,4]
print(d.index(9))

#count method
a=[4,7,8,9,7,6]
print(a.count(7))

#sort method
a=[4,9,8,7]
a.sort()
print(a)

#sort reverse method
g=[3,7,9,10,8]
g.sort(reverse=True)
print(g)

#reverse method
a=[2,8,7,6,5]
a.reverse()
print(a)

#copy method
g=[3,5,7,8,]
m=g.copy()
print(m)

#slicing method
numbers=[10,30,50,46,87]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

#problems
a=int(input("Enter minutes"))
print("hours:",a/60)
print("remaining minutes:",a%60)
print("total seconds:",a*60)

#power calculation
base=int(input("base:"))
power=int(input("power:"))
print(base ** power)

#total and avg of numbers
n1=int(input("enter number:"))
n2=int(input("Enter number:"))
n3=int(input("Enter number:"))
total=n1+n2+n3
avg=total/3
print("Total:",total)
print("avg:",avg)

#greater then comparisison 
a=int(input("Enter number:"))
b=int(input("Enter number:"))
print("grater:",a>b)

#equality check
n1=int(input("enter number:"))
n2=int(input("enter number:"))
print("equal:",n1==n2)

