#if only a successfull execution statement is there then only else statement is used in loop
#Break

#Question is 1 to 100 but come out at 50
for i in range(1,101):
    if i==50:
        break
    print(i,end=' ')
#--------------------------------------------
# continue
for i in range(1,101):
    if i==50:
        continue
    print(i,end=" ")

#--------------------------------------------------------------
# pass    
for i in range(1,101):
    if i==50:
        pass  #purely a null statement or empty class
    print(i,end=" ")    
#------------------------------------------------------------------------
#functions

def function1():
    print("it is a function1")
function1()
#------------------------------------------------------------------------------------------------
def function2(num1,num2):
    print("num1",num1,"num2",num2)
function2(10,20)
#print()__str__ it is being called when we have data other than string which explicitly convert into string
#-------------------------------------------------------------------------------------------------------------
def function3(num1,num2):
    num3=num1+num2
    return num3
    #print("num1",num1,"num2",num2)
print("value returned",function3(100,200))

#--------------------------------------------------------------
def function4(num1,num2):
    num3=num1+num2
    return num3
    #print("num1",num1,"num2",num2)
print("value returned",function4(10,20.2))

#------------------------------------------------------------------

def function5(num1,num2):
    num3=float(num1)+num2  #explicitly typecasted
    return num3   
print("value returned",function5('10',20.2))
#--------------------------------------------------------------------
def function6(num1,num2):
    num3=num1+str(num2)  #explicitly typecasted
    return num3   
print("value returned",function6('10',20.2))
#---------------------------------------------------------------------

