#categories of functions
#based on arguments

#1: positional arguments
def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(10,20,30,40)
function1(100,200,300,400)
function1(100,"200",300,400)

#2: Keyword arguments

def function2(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4=10,num1=20,num2=30,num3=40)
function2(num4=10,num1=20,num2=10,num3=40)

#3: Default arguments   #default value should be at right

def function3(name,rollno,branch,collegename):
    print(name,rollno,branch,collegename)
function3("sathweeka",54,"ECE","GIET")
function3("akhila",48,"ECE","GIET")
function3("harsha",328,"CSE","GIET")
function3("aditya",244,"CST","GIET")

#-----------------------------------------------------

def function3(name,rollno,branch,collegename="GIET"):
    print(name,rollno,branch,collegename)
function3("sathweeka",54,"ECE")
function3("akhila",48,"ECE",)
function3("harsha",328,"CSE",)
function3("aditya",244,"CST",)

#------------------------------------------------------------

def function3(name,rollno,branch="ECE",collegename="GIET"):
    print(name,rollno,branch,collegename)
function3("sathweeka",54)
function3("akhila",48,)
function3("harsha",328,"CSE")
function3("aditya",244,"CST")


#4: Variable no. of arguments

def function4(*var): #(*var) is tuple= represents elements of a tuple
    for i in var:
        print(i,end=' ')
function4(10,20)
print() #print() for new line
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)
print()
#-------------------------------------

def add(*var):
    sum1=0
    for i in var:#10,20
        sum1=sum1+i
        print(sum1)
add(10,20)
print() #print() for new line
add(10,20,30,40)
print()
add(10,20,30,40,50,60)
print()
#--------------------------------------------

def add(*var):
    sum1=0
    for i in var:#10,20
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30,40))
print(add(10,20,30,40,50,60))
#----------------------------------------------------
'''
write a python program to find and display the product of three positive integer values based on the rule mentioned below:
It should display the product of the three values except when one of the input is 7. In that case, 7 should not be included in the product and the values to its left also should not be included.
If there is only one value to be considered, display that values itself. If no values can be included in the product, display -1.
note: assume that if 7 is one of the positive integer values, then it will occur only once.
sample input                    sample output
1,5,3                               15
3,7,8                               8
7,4,3                               12
1,5,7                               -1



'''
#ans
num1=int(input())
num2=int(input())
num3=int(input())
if num1==7:
    print(num2*num3)
elif num2==7:
    print(num3)
elif num3==7:
    print(-1)
else:
    print(num1*num2*num3)


#-----------------------------------------------------------------------------------
'''
A traveller on a visit to India is in need of some Indian Rupees (INR) but he has money belonging to another currency.
Write a python program to implement a currency calculator which accepts the amount needed in INR and the name of the currency which the traveller has.
Currency                                    Equivalent of 1.00 INR
Euro                                          0.01417
British Pound                               0.0100
Australian                                   0.02140
Canadian Dollar                              0.02027
'''
#ans

def currencycal(AmountINR,curr):
    if curr=="Euro":
        print(AmountINR*0.01417)
    elif curr=="British Pound":
        print(AmountINR*0.0100)
    elif curr=="Australian":
        print(AmountINR*0.02140)
    elif curr=="Canadian Dollar":
        print(AmountINR*0.02027)
    else:
        print(-1)
currencycal(300,"Euro")
currencycal(300,"British Pound")
currencycal(300,"Australian")
currencycal(300,"Canadian Dollar")

#---------------------------------------------------------------------------------------------

'''
The flight ticket rates for a round-trip (mumbai->dubai) were as follows:
Rate per Adult: Rs. 37550.00
Rate per child: 1/3rd of the rate per adult
Service Tax: 7% of the ticket amount (including all passengers)
As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
Find and display the total ticket cost for a group which had adults and children.

sample input                                  expected output
Number of adults     Number of children        Ticket cost
  5                       3                     204910.35
  3                       1                     120535.5
'''

#ans

n_adults=int(input("Enter the number of adults: "))
n_childs=int(input("Enter the number of childs: "))
total=((n_adults*37550.0)+(n_childs*37550.0/3))
print(total)
total1=total*0.07
total2=total+total1
print("with ur service tax",total2)
total_amount=total*0.90
print(total_amount)


#-------------------------------------------------------------------

n_adults=int(input("Enter the number of adults: "))
n_childs=int(input("Enter the number of childs: "))
print((((n_adults*37550.0)+(n_childs*37550.0/3)*1.07)*0.90))
'''print(total)
total1=total*0.07
total2=total+total1
print("with ur service tax",total2)
total_amount=total*0.90
print(total_amount)'''

#-----------------------------------------------------------------

'''
you have x no. of 5 rupee coins and y no. of 1 rupee coins.
you want to purchase an item for amount z. the shopkeeper wants you to provide the exact change.
you want to pay using minimum number of coins. how many 5 rupee coins and 1 rupee coins will you use?
if exact change is not possible then display -1.
sample input                                                                                      expected output   
available Rs. 1 coins         available Rs.5 coins notes         Amount to be made        Rs.1 coins needed        Rs.5 notes needed       
    2                                  4                                21                      1                           4
    11                                 2                                11                      1                           2
    3                                  3                                19                               -1           


#ans
x=int(input("Available Rs.5 notes are: "))
y=int(input("Available Rs.1 coins are: "))
z=int(input("Amount to be made is: "))
if ((x*5+y*1)<z):
    print("Amount not available")
    
'''
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    five = int(rupees_to_make/5)
    one_needed = rupees_to_make%5
    five_needed = five if five <= no_of_five else no_of_five
    if (five > no_of_five):
        one_needed = rupees_to_make - 5 * no_of_five     
    
    (print("No. of Five needed : {}\nNo. of One needed  : {}".format(five_needed,one_needed))) if one_needed <= no_of_one else (print(-1))

make_amount(int(input()),int(input()),int(input()))
