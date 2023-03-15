#Python programming
#Datatypes
name="sathweeka"#explicitly declared at run time
print("name",name,type(name))
#full pledge object oriented
rollno=54
print("rollno",rollno,type(rollno))
percentage=88.9
print("percentage",percentage,type(percentage))
student_y_no=True
complex_number=3+6j
print("complex_number",complex_number,type(complex_number))


#Decision making statements


#read a number ---> multiple 3---> multiple of 5 ---> if both then print multiple of 3&5 else print invalid
a=int(input())
if (a&3==0 and a%5==0):
    print("multiple of both 3 and 5")
elif (a%5==0):
    print("multiple of 5")
elif (a%3==0):
    print("multiple of 3")
else:
    print(invalid)

#range function

#1 to 100
for i in range(1,101):# range(start,end,step)
    print (i,end=' ')
#print(*no of objects, step=' ',end='\n')
#odd numbers between 1 to 100

for i in range(1,101,2):
    print(i,end=' ')
print()
#even numbers between 1 to 100

for i in range(2,101,2):
    print(i,end=' ')
    
# numbers in reverse order
for i in range(100,0,-1):# range(start,end,step)
    print (i,end=' ')
print()
#odd numbers between 100 to 1

for i in range(99,0,-2):
    print(i,end=' ')
print()
#even numbers between 100 to 1

for i in range(100,1,-2):
    print(i,end=' ')


