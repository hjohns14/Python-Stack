
num1 = 42 #Variable Declaration # Data Type Number # init
num2 = 2.3 # Variable Declaration # Data Type Number # init
boolean = True # Variable Declaration# Data Type Boolean # init
string = 'Hello World' # Variable Declaration # Data Type String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Variable Declaration # Data Type List # init
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Variable Declaration # Data Type Dictionary # init
fruit = ('blueberry', 'strawberry', 'banana') # Variable Declaration # Data Type Tuple # init
print(type(fruit)) #log Statement , Type check
print(pizza_toppings[1]) #log Statement, list access value
pizza_toppings.append('Mushrooms') # List add value
print(person['name']) # Dictionary access value / log statement
person['name'] = 'George' # Dictionary change value
person['eye_color'] = 'blue' # Dictionary change value
print(fruit[2]) #log statement / tuple access value

if num1 > 45: # if 
    print("It's greater") # Log Statement
else: # else
    print("It's lower") # Log Statement

if len(string) < 5: # if
    print("It's a short word!") # Log Statement
elif len(string) > 15: # else if
    print("It's a long word!") # Log Statement
else: # else
    print("Just right!") # Log Statement

for x in range(5): # for Start = 0 End = 5
    print(x) # Log Statement
for x in range(2,5):  # for Start = 2 End = 5
    print(x) # Log Statement
for x in range(2,10,3):  # for Start = 2 End = 10 increment = 3
    print(x) # Log Statement
x = 0
while(x < 5): #while start x = 0 end x >= 5
    print(x) # Log Statement
    x += 1 # While Increment

pizza_toppings.pop()  # List delete last item
pizza_toppings.pop(1) # List Delete item at index 1

print(person) # Log Statement
person.pop('eye_color') # Dictionary Delete item "eye_color"
print(person) # Log Statement

for topping in pizza_toppings: # for statement, sequence
    if topping == 'Pepperoni': # if
        continue # continue
    print('After 1st if statement') # Log Statement
    if topping == 'Olives': #if
        break #break

def print_hello_ten_times(): #Function No parameter
    for num in range(10): #for start = 0 end = 10
        print('Hello') # Log Statement

print_hello_ten_times() # call function

def print_hello_x_times(x): # function with parameter x
    for num in range(x): # for start = 0 end = x
        print('Hello') # Log Statement

print_hello_x_times(4) #call function

def print_hello_x_or_ten_times(x = 10): # Function with parameter x with default value of 10
    for num in range(x): # for start = 0 end = x
        print('Hello') # Log Statement

print_hello_x_or_ten_times() # call function (x=10)
print_hello_x_or_ten_times(4) # call function (x=4)


"""
Bonus section # Multiline Comment
"""

# print(num3) , NameError
# num3 = 72  , Number asignment
# fruit[0] = 'cranberry' , TypeError
# print(person['favorite_team']), KeyError
# print(pizza_toppings[7]) IndexError
#   print(boolean) , IndentationError
# fruit.append('raspberry') # AttributeError (append)
# fruit.pop(1) , AttributeError (pop)