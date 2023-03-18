'''
write a python function, nearest_palindrome() which accepts a number and
returns the nearest palindrome greater than the given number.
sample input                expected output
  99                           101
  1221                         1331
'''
'''
#ans

def nearest_palindrome(num):
    num+=1
    while str(num)!= str(num)[::-1]:
        num += 1
    return num
num=int(input())
print(nearest_palindrome(num))

#-----------------------------------------------------------------------------

Care hospital wants to know the medical speciality visited by the maximum
number of patients. assume along with the medical speciality visited by the
patient is stored in a list. the details of the medical specialities are stored
in a dictionary as follows:
{"P":"Pediatrics","O":Orthopedics","E":"ENT"}
write a function to find the medical speciality visited by the maximum number
of patients and return the name of the speciality.
note:
1.assume that there is always only one medical speciality which is visited by
maximum number of patients.
2.perform case sensitive string comparison wherever necessary.
sample input                                        expected output
[101,P,102,O,302,P,305,P]                             Pediatrics
[101,O,102,O,302,P,305,E,401,0,656,0]                 orthopedics
[101,O,102,E,302,P,305,P,401,E,656,0,987,E]             ENT


#ans

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    max_visit=0
    P=patient_medical_speciality_list.count('P')
    E=patient_medical_speciality_list.count('E')
    O=patient_medical_speciality_list.count('O')
    if P>E and P>O:
        speciality= medical_speciality['P']
    elif E>O:
        speciality= medical_speciality['O']
    else:
        speciality= medical_speciality['O']
    return speciality
patient_medical_speciality_list=[301,'P',302,'P',305,'P',401,'E',656,'E']
medical_speciality={'P' : 'Pediatrics','O' : 'Orthopedics','E' : 'ENT'}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
#------------------------------------------------------------------------------------


write a python program to display all the common characters between two strings.
return -1 if there are no matching characters.
note: ignore blank spaces if there are any.
perform the case sensitive string comparison wherever necessary.
sample input                             expected output
"I like Python"
"Java is a very popular language"         lieyon

#ans

def common_char(str1,str2):
    str=""
    for i in str1:
        if i in str2:
            if i not in str:
                str=str+i
    if(str):
        return str.replace(" "," ")
    else:
        return -1
str1=str(input())
str2=str(input())
print(common_char(str1,str2))
'''
#----------------------------------------------------------
'''class Employee:
    def __init__(self):
        self.employee_id = None
    def check_eligibility(self):
        if(self.employee_id>=9000 and self.employee_id<=10000):
            print("The employee is eligible for special benefits")
        else:
            print("The employee is not eligible for special benefits")
emp1=Employee()
emp1.employee_id=10000
emp1.check_eligibility()
emp2=Employee()
emp2.employee_id=4500
emp2.check_eligibility()
#---------------------------------------------------
class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
#--------------------------------------------------------------

class Example:
    def __init__(self,num):#num is local variable
        self.num=num#self.num is instance variable
    def set_num(self,num):
        num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())

#--------------------------------------------------------------

class Customer:
    def __init__(self):
        cust_id=100                 #attribute error
c1=Customer()
print(c1.cust_id)

#------------------------------------------------------------------

class Customer:
    def __init__(self,id):
        id=100                 #attribute error
c1=Customer(200)
print(c1.id)
#-----------------------------------------------------------------
class Customer:
    def __init__(self,id):
        self.id=100                 
c1=Customer(200)
print(c1.id)

#---------------------------------------------------------------

class Customer:
    def __init__(self,id):
        self.id=id                 
c1=Customer(200)
print(c1.id)

#-----------------------------------------------------------------

class Book:
    def __init__(self):
        self.title=None
my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn Python the hard way"
my_fav.title="Learning Python"
print("My favorite is",my_fav.title)
print("Your's is",your_fav.title)
print("Your's is",your_fav)
'''
#-----------------------------------------------------------
'''
class Example:
    def __init__(self,num1):
        self.num=num1
    def set_num(self,num2):
        self.num=num2
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
'''
#--------------------------------------------------------------------
class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material
s1=Shoe(1000, "Canvas")
print(s1)
print(s1.price,s1.material)
#-----------------------------------------------------
class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material
s1=Shoe(1000, "Canvas")
print(s1)
print("the unique id of the object",id(s1))
#-------------------------------------------------------

class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material
    def __str__(self):
        return "Shoe with price: " + str(self.price) + " and material: " + self.material
s1=Shoe(1000, "Canvas")
print(s1)

#--------------------------------------------------------------------

class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    def purchase(self):
        self.display()
        print("Calculating price")
Mobile().purchase()
#------------------------------------------------------------
'''class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")
    def purchase(self):
        self.display()
        print("Calculating price")
m1=Mobile()
print(m1)
m2=Mobile()
print(m2)
m1=m2
print(m1)'''
#--------------------------------------------------------------

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        self.total_price = None
    def purchase(self):
        if self.brand == "Apple":
            discount = 10
        else:
            discount = 5
        self.total_price = self.price - self.price*(discount / 100)
        print("Total price of", self.brand, "mobile is", self.total_price)
    def amount_returned(self):
        return (self.price-self.total_price)
        
mob1=Mobile("Apple", 20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()
print(mob1.amount_returned())
print(mob2.amount_returned())
        
#-------------------------------------------------------------------------------

class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance
    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount
    def show_balance(self):
        print("The balance is ",self.wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()
#-------------------------------------------------------
'''
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance #for private use __
    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount
    def show_balance(self):
        print("The balance is ",self.wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
print(c1.__wallet_balance)       #error because it is outside class

c1.show_balance()
'''
#---------------------------------------------------------
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance #for private use __
    def set_balance(self, amount):
        if amount < 50000 and amount > 0:
            self.__wallet_balance += amount
    def get_wallet_balance(self):
        return self.__wallet_balance
        
c1=Customer(100, "Gopal", 24, 1000)
print(c1.get_wallet_balance())      
c1.set_balance(5000)
print(c1.get_wallet_balance())
#---------------------------------------------------------------------

class Dam:
    def __init__(self, name, length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("Dam Length", dam1.get_length())
#----------------------------------------------
class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(False, True)
print(rate)
#---------------------------------------------------------
class Table:
    def __init__(self):
        print(id(self))
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
dining_table=Table()
print("dining_table id is:",id(dining_table))
back_table=Table()
print("back_table id is:",id(back_table))
front_table=back_table
back_table=dining_table
print(dining_table,back_table,front_table)
print(id(dining_table),id(back_table),id(front_table))
print("dining_table:",id(dining_table))
print("back_table:",id(back_table))
print(id(front_table))

#-------------------------------------------------------------------------
