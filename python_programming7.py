#opps questions
'''
WeCare insurance company wants to calculate premium of vehicles.
-->vehicles are of two types - "Two Wheeler" and "Four Wheelers
each vehicle is identified by vehicle id, type, cost and premium amount.
--> Premium amount is 2% of the vehicle cost for two wheelers and
6% of the vehicle cost for four wheelers.
calculate the premium amount and display the vehicle details.
write a python program to implement the class chosen with its attributes and methods.
Note:
consider all instance variables to be private and methods to be public
include getter and setter methods for all instance variables , display appropriate error message,
error message, if the vehicle type is invalid
perform case snsitive string comparison
represent few objects of the class, initialize instance variables using setter methods,
 invoke appropriate methods and test your program.
 
#ans

class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
        print(self.__vehicle_id)
    
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
        print(self.__vehicle_type)
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
        print(self.__vehicle_cost)
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
        print(self.__premium_amount)
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def get_premium_amount(self):
        return self.__premium_amount
    def calculate_premium(self):
        if self.__vehicle_type=="Two Wheeler":
            self.__premium_amount=self.__vehicle_cost*0.02
        elif self.__vehicle_type=="Four Wheeler":
            self.__premium_amount=self.__vehicle_cost*0.06
    def display_vehicle_details(self):
        self.calculate_premium()
        print("the vehicle id is : ",self.__vehicle_id)
        print("The vehilcle type :" ,self.__vehicle_type)
        print("The vehicle cost is:",self.__vehicle_cost)
        print("The vehicle premium is:",self.__premium_amount)
s1=Vehicle()
s1.set_vehicle_id(121)
s1.set_vehicle_type("Two Wheeler")
s1.set_vehicle_cost(60000)
s1.calculate_premium()
s1.display_vehicle_details()
#----------------------------------------------------------------------------------
a university wants to automate their admission process.
 students are admitted based on marks scored in a qualifying exam.A student is identified by student_id,age and marks in qualifying exam.
 data are valid if:
     age is greator than 20
     marks is between 0 and 100(both inclusive)
     a student qualifies for admission, if
     age and marks are valid and marks is 65 or more
     write a python program to represent the students seeking admission in the university.
    RULES TO FOLLOW
    the details of student class are given below.
    Class name:student
    attributes :(private)
    student_id
    marks
    age methods:-(public) _init_(), validate_marks(),validate_age(),check_qualification()
    continuing with the previous scenarios, a student eligible for admission has to choose a course and pay the fees for it. if they have scored more than 85 marks in qualifying
    exam, they get 25% discount on fees.
    valid course ids and fees are given below:
        course id        fees
        1001             25575.0
        1002             15500.0

#ans


class Student:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
        self.__fees=None
    def set_student_id(self,student_id):
        self.__student_id=student_id
        print(self.__student_id)
    
    def set_marks(self,marks):
        self.__marks=marks
        print(self.__marks)
    def set_age(self,age):
        self.__age=age
        print(self.__age)
    def set_fees(self,fees):
        self.__fees=fees
        print(self.__fees)
    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    def get_fees(self):
        return self.__fees
    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self.__marks>65:
                print("you are eligible for admission")
                
            else:
                print("you are not eligible for admission")
        else:
            print("Invalid")
    def score(self):
        if self.__marks>85:
            self.__fees=self.__fees-(self.__fees*0.25)
        else:
            return self.__fees
        print("Your fees is:",self.__fees)

s1=Student()
s1.set_student_id(121)
s1.set_marks(89)
s1.set_age(26)
s1.set_fees(25575.0)
s1.check_qualification()
s1.score()

'''


#-----------------------------------------------------------------------------

'''
 PizzaForYou is a pizza store which sells different kinds of pizzas based on
 customer's order.40 min
 Customer can either collect the order in person or opt for a door delivery.
 Write a python program based on the class diagram given below?
 Customer class validate_quantity(): A customer can order 1 to 5 pizzas
 If quantity is valid, return true. Else return false
 Pizzaservice class:
 Initialize static variable counter to 100
 Attribute, additional_topping is a boolean value which indicates whether additional topping is required or not.
 True – additional topping is required, False – additional topping is not required
 validate_pizza_type(): Customers can order "small" or "medium" type pizzas
 If pizza type is valid, return true. Else return false
 calculate_pizza_cost(): Calculate pizza cost
 Validate pizza type and quantity
 If valid,
 Identify pizza cost based on details mentioned in the table
 Set attribute, pizza_cost with the calculated pizza cost
 Auto-generate service_id starting from 101 prefixed by first letter of pizza type. Example – S101, s102, m103, S104, M105 etc
 If invalid, set pizza_cost to -1
 PizzaType	Cost/Pizza(in Rs)	Additional topping cost/Pizza       (in Rs), if applicable
 Small	150	35
 Medium	200	50
 Doordelivery class:
 validate_distance_in_kms(): Minimum distance for door delivery is 1km and maximum is 10kms
 Validate distance_in_kms
 If valid, return true. Else, return false
 calculate_pizza_cost: Calculate pizza cost
 Validate distance in kms
 If valid,
 Calculate pizza cost (Hint: Invoke overridden method in parent class)
 If pizza_cost is not -1, identify delivery charge based on details mentioned below and add it to attribute, pizza_cost
 Distance in kms	Delivery Charge in km(in Rs)
 For first 5 kms	5
 For remaining 5 kms	7
 Else, set pizza_cost to -1
 Note: Perform case insensitive string comparison  
 For testing:
 Create objects of Pizzaservice and Doordelivery classes
 Invoke calculate_pizza_cost() on Pizzaservice and Doordelivery objects
 Display the detail

class Customer:
    def __init__(self):
        self.__customer_id=None
        self.__quantity=None
        self.__additional_topping=None
        self.__pizza_type=None
        self.__pizza_cost=None
        self.__service_id=None
    def set_customer_id(self,customer_id):
        self.__customer_id=customer_id
        print(self.__customer_id)
    
    def set_quantity(self,quantity):
        self.__quantity=quantity
        print(self.__quantity)
    def set_additional_topping(self,additional_topping):
        self.__additional_topping=additional_topping
        print(self.__additional_topping)
    def set_pizza_type(self,pizza_type):
        self.__pizza_type=pizza_type
        print(self.__pizza_type)
    def set_pizza_cost(self,pizza_cost):
        self.__pizza_cost=pizza_cost
        print(self.__pizza_cost)
    
    def set_service_id(self,service_id):
        self.__service_id=service_id
        print(self.__service_id)
    def get_customer_id(self):
        return self.__customer_id
    def get_quantity(self):
        return self.__quantity
    def get_additional_topping(self):
        return self.__additional_topping
    def get_pizza_type(self):
        return self.__pizza_type
    def get_pizza_cost(self):
        return self.__pizza_cost
    def get_service_id(self):
        return self.__service_id
    def validate_quantity(self):
        if self.__quantity<=1 and self.__quantity>=5:
            return True
        else:
            return False
s1=Customer()
s1.set_customer_id(121)
s1.set_quantity(1)
s1.set_additional_topping(bool(input("Do you like additional_topping? True or False?")))
s1.set_pizza_type("small")
s1.set_pizza_cost(150)
s1.set_service_id(12321)#random.randint(1, 100000000)
s1.validate_quantity()
'''
types=['small','medium','small','medium']
class Customer:
    def __init__(self, customer_name, quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity
    def validate_quantity(self):
        if self.__quantity in range(1,6):
            return True
        else:
            return False
    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity
    
class Pizzaservice:
    counter=100 #it is counter which is static
    def __init__(self, customer, pizza_type, additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=0
        self.__service_id=None
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in types:
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer.validate_quantity(self.__customer):
            print("pizza")
            if self.__pizza_type == "small":
                self.pizza_cost=150 * Customer.get_quantity(self.__customer)
                if self.__additional_topping:
                    self.pizza_cost+=35 * Customer.get_quantity(self.__customer)
            if self.__pizza_type == "medium":
                self.pizza_cost=200 * Customer.get_quantity(self.__customer)
                print("hi")
                if self.__additional_topping:
                    self.pizza_cost+=50 * Customer.get_quantity(self.__customer)
            if not self.__service_id:
                self.__service_id = self.__pizza_type[0] +str(Pizzaservice.counter+1)
                Pizzaservice.counter+=1
        else:
            self.pizza_cost=-1
    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__customer
    def get_additional_topping(self):
        return self.__additional_topping
    
class Doordelivery(Pizzaservice):
    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        self.__delivery_charge=0
        self.__distance_in_kms=distance_in_kms
        Pizzaservice.__init__(self, customer, pizza_type, additional_topping)
    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range(1,11):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            Pizzaservice.calculate_pizza_cost(self)
            if self.pizza_cost!= -1:
                distance=1
    
                while(distance<=self.__distance_in_kms):
                    if distance in range(1,6):
                        self.pizza_cost += 5
                    if distance in range(6,11):
                        self.pizza_cost += 7
                    distance += 1
        else:
            self.pizza_cost = -1
    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms
c = Customer("Sai", 5)
print(c.get_customer_name())
p1 = Pizzaservice(c, "medium", True)
p1.calculate_pizza_cost()
print(p1.pizza_cost)
print(p1.get_service_id())

d1 = Doordelivery(c, "medium", True,6)
d1.calculate_pizza_cost()
print(d1.pizza_cost)
print(d1.get_service_id())


'''
bounded method call & unbounded method call
'''
