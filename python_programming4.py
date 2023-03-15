#Pre-defined datastructures
#List --> ordered--default index
list1=[]
print(list1,type(list1))
list2=[10,20,30,40]
print(list2,type(list2))
list3=[10,20.2,30+3j,True,"python"]
print(list3,type(list3))
list4=list([100,200,300,400])
print(list4,type(list4))
list4.append(501)
print(list4,type(list4))
list4.extend([601,701,801])
print(list4,type(list4))
list4.insert(0,51)#index,value
print(list4,type(list4))
list4.insert(4,350)#index,value
print(list4,type(list4))
list4.remove(801)#index,value
print(list4,type(list4))
list4.pop(0)#index,value
print(list4,type(list4))
list4.pop(0)#index,value
print(list4,type(list4))
del list4[1]
print(list4,type(list4))
#--------------------------------------------------------
'''
write a python function which accepts a sentence and finds the number of letters and digits in the sentence.
it should return a list in which the first value should be letter count and the second value should be digit count.
ignore the spaces or any other special character in the sentence.
sample input                 expected output
Infosys 123                    [7,3]
ABCEFG                         [6,0]
'''
#ANS

def function(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return [l_count, d_count]
print(function("Infosys 123"))
#print(function(input()))   
#--------------------------------------------------------------------

'''
write a python function, find_pairs_of_numbers() which accepts a list of positive integers ith no repetitions and returns count of pairs of numbers in the list that adds up to n.
the function should return 0, if no such pairs are found in the list.
sample input                         expected output
[1,2,7,4,5,6,0,3],6                           3 (1,5)(2,4)(6,0)
[3,4,1,8,5,9,0,6],9                           4 (3,6)(4,5)(1,8)(9,0)
'''
#ans

def find_pairs_of_numbers(num_list,n):
    count=0
    for x in num_list:
        index=num_list.index(x)+1 #index=1
        for y in range(index,len(num_list)):
            if x+num_list[y]==n: #1+2==6
                count+=1  #count=0
    return count
num_list=[1,2,7,4,5,6,0,3]
n=6#int(input())
print(find_pairs_of_numbers(num_list,n))
#-------------------------------------------------------------------------
'''
write a python function which accepts a string and returns a string made of the first 2 and the last 2 characters of the given string. if the string length is less than 2, return -1.
note: if the string length is equal to 2, consider the 2 characters to be the first as well as the last two characters.
sample input             expected output
w3resource                  w3ce
A                            -1
'''
#ans

def word(str1):
    if len(str1)<2:
        return -1
    else:
        return str1[0:2]+str1[-2:]
print(word("water"))
print(word(input()))

#-----------------------------------------------------------------------------------

'''
write a python function to add 'ing' at the end of a given string and return the new string.
if the given string already ends with 'ing' then add 'ly'.
if the length of the given string is less than 3, then leave it unchanged.
sample input             expected output
sleep                       sleeping
amazing                     amazingly
is                            is
'''
#ans

def function(str1):
    if len(str1)<3:
        return str1
    elif str1[-3:]=="ing":
        return str1+"ly"
    else:
        return str1+"ing"
print(function("amazing"))
#print(function(input()))
#-------------------------------------------------------------------------------------

'''
write a python function,check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.
1. the number and its double should have exactly the same number of digits.
2. both the numbers should have the same digits, but in different order.
otherwise it should return False.
example: if the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.
'''
#ans
def check_double(number):
    num_str = str(number)
    double_str = str(number*2)
    if len(num_str)!=len(double_str):
        return False
    for digit in num_str:
        if digit not in double_str:
            return False
    for digit in num_str:
        if num_str.count(digit)!=double_str.count(digit):
            return False
    return True
print(check_double(125874))
#print(check_double(input()))
#------------------------------------------------------------------------------
def check_double(number):
    num_str = str(number)     #125874
    double_str = str(number*2) #251748
    count=0
    for x in num_str:
        if x in double_str:
            count+=1
        else:
            return False
    if count==len(num_str):
        return True
print(check_double(125874))
print(check_double(245))
#----------------------------------------------------------------------------

'''
a teacher is in the process of generating few reports based on the marks scored by the students of her class in a project assessment.
assume that the marks of her 10 students are available in a tuple. the marks are out of 25.
write a python program to implement thefollowing functions:
1. find_more_than_average():find and return the percentage of students who have
scored more than the average marks of the class.
2.generate_frequency(): find how many students have scored the same marks.
for example, how many have scored 0, hw many have scored 1, how many have scored 3....how many have scored 25.
the result should be populated in a list and returned.
3. sort_marks(): sort the marks in the increasing order from 0 to 25. the sorted values should be populated in a list and returned.
sample input                                    expected output
list_of marks =(12,18,25,24,2,5,18,20,20,21)           70.0

                                  [0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,2,0,2,1,0,0,1,1]

                                  [2,5,12,18,18,20,20,21,24,25]
'''
#ans
marks=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_average():
    avg= sum(marks)/len(marks)
    count =0
    for mark in marks:
        if mark > avg:
            count=count+1
    return (count/len(marks))*100
def sort_marks():
    return sorted(marks)
def generate_frequency():
    freq=[]
    for mark in range(0,26):
        count=0
        for y in marks:
            if mark==y:
                count+=1
        freq.append(count)
    return freq
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
#-----------------------------------------------------------------------------   
'''
represent a small bilingual (english-swedish) glossary given below as a python dictionary
{"merry":"god,","chirstmas":"jul,","and":"och","happy":"gott","new":"nytt","year":"ar"}
and use it to translate your chirstmas wishes from english into swedish.
that is, write a python function translate() that accepts the bilingual dictionary and a list of
english words (your christmas wish) and returns a list of equivalent swedish words.
'''
#ans
def translate(dict1,list1):
    list2=[]
    for i in list1:
        list2.append(dict1[i])
    return list2
dict1={"merry":"god,","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
list1=["merry","christmas"]
print(translate(dict1,list1))
#-------------------------------------------------------------------------------

'''
find the number of distinct subarrays in an array of position integers such
that the sum of the subarray is an odd integer, two subarray are considered different
if they start or end at different index input.

1
3
1 2 3
[1]  [1 2]  [1,2,3]  [2]  [2,3]  [3]
4
'''
#ans

n1=int(input())
n2=int(input())
'''result=[]
for i in range(n1,n2+1):
    result.append(i)
print(result)
result=[i for i in range(n1,n2+1)]
print(result)'''
array=[i for i in range(n1,n2+1)]
print(array)#[1,2,3]
result=[]
for i in range(len(array)):#i=1
    for j in range(i,len(array)):#j=1,2
        result.append(array[i:j+1])#[0:1]=[1],
print(result)                       #[0:2]=[1,2]
#----------------------------------------------------------------------------
#list comprehension for creating sub array
result=[array[i:j+1] for i in range(len(array)) for j in range(i,len(array))]
print(result)
#---------------------------------------------------------------------------------
c=0
for i in result:
    if sum(i)%2!=0:
        c+=1 #c=4
print(c)
