#List comprehension
'''
#for loop version

result=[]
for i in range(11):
    result.append(i)
print(result)

#list comprehension version

print([i for i in range(11)])
#for loop version --> odd elements

result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
print(result)
#list comprehension version --> odd elements
print([i for i in range(11)if i%2!=0]) #syntax-output inner_loop_with_range condition
print([i for i in range(11)if i%2==0])
#for loop version -->even elements square
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
#list comprehension version -->even elements square
print([i if i%2!=0 else i**2 for i in range(11)])

#--------------------------------------------------------------------------------
#matrix 2D data
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop version --> odd then square if it is even cube it
result=[]
for row in mat:
    row_element=[]
    for element in row:
        if element%2!=0:
            row_element.append(element**2)
        else:
            row_element.append(element**3)
    result.append(row_element)
print(result)
#list comprehension-->odd then square if it is even then cube

print([element**2 if element%2!=0 else element**3 for row in mat
       for element in row])             #syntax-condition outer_loop inner_loop
print([[element**2 if element%2!=0 else element**3 for element in row]
       for row in mat])
'''
#-------------------------------------------------------------------------------

'''
for each number in list_b, get the number and its position(index) in mylist as are turn
list of tuples.
sample input
mylist = [9,3,6,1,5,0,8,2,4,7]
list-b = [6,4,6,1,2,2]
sample output
result = [(6,2),(4,8),...]
'''
#ans
'''
mylist = list[input()]
print(mylist)
list_b = list[input()]
print(list_b)'''
mylist = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]
#mylist = list(input())
#list_b = list(input())
result=[]
for element in list_b:
    result.append((element,mylist.index(element)))
print(result)
print([(element,mylist.index(element))for element in list_b])
#--------------------------------------------------------------
#dictionary comprehension
#for loop version dictionary
mylist = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]
result={}
for i in list_b:
    result[i]=mylist.index(i)
print(result)
#--------------------------------
print({i:mylist.index(i) for i in list_b})#dict comprehension
#----------------------------------------------------------------
'''
the goal is to tokenize the following 5 sentences into words, excluding the stop words.
input:
sentences = ["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday",
"with over three lakh diya or earthen lamps","lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for','was', 'a','the','and','to','in','on','with']
'''
#ans
sentences = ["a new world record was set",
             "in the holy city of ayodhya",
             "on the eve of diwali on tuesday",
             "with over three lakh diya or earthen lamps",
             "lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for','was', 'a','the','and','to','in','on','with']
result=[]
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word)
    result.append(row_data)
print(result)

#list comprehension
print([[word for word in sentence.split() if word not in stopwords]for sentence in sentences])

#------------------------------------------------------------------------------------------
'''
input: a string of comma separated numbers. the number 5 and 8 are present in the list.
assume that 8 always comes after 5.
case1: num1 = add all the numbers which do not lie between 5 and 8 in the input
case2: num2 = number formed by concatenating all numbers from 5 to 8
output sum of num1 and num2
example
1)3,2,6,5,1,4,8,9

num1 = 3+2+6+9=20
num2 = 5148
o/p = 5148+20=5168

array=list(map(int,input().split(",")))
number1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
number2=""
for i in l:
    number2+=str(i)
print(int(number2)+number1)'''
#------------------------------------------------------------------------------

'''
string rotation
input:  rhdt:246,ghftd:1246
exp1: here every string is associated with the number sep by:
--> if sum of squares of digits is even then rotate the string by 1
--> if sum of squares of digits is odd then rotate the string left by 2 position
2*2+4*4+6*6=56 which is even so rhdt = trhd
1*1+2*2+4*4+6*6=57 which is odd so rotate left by 2 so ghftd=ftdgh
'''
#ans
s=input().split(",")
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)#stt=[rhdt,ghftd]
    numm.append(n)#numm=[246,1246]
def rotate (ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1] #rhdt   t+rhd
    else:
        return ss[2:]+ss[:2] # ghftd   ftdgh
for i in range(len(numm)): #i=0
    print(rotate(stt[i],numm[i]))
   
#-------------------------------------------------------------------------------
'''
given a number n, write a program to find the sum of the largest prime factors of
each of nine consecutive numbers starting from n.
g(n) = f(n)+f(n+1)+f(n+2)+f(n+3)+f(n+4)+f(n+5)+f(n+6)+f(n+7)+f(n+8)
where, g(n) is the sum and f(n)is the largest prime factor of n
for example,
g(10)=f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18)
     = 5 +11 +3 +13 +7 +5 +2 +17 +3
     =66
'''
#ans
n=int(input())


