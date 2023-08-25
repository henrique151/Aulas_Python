#=============Pergunta 2:

print(len("95637+12")) 

#R: 8

#=============Pergunta 3:

#Read the code below, what will be printed in the output?

score = 67
if score < 80 and score > 70:
    print("A")
elif score < 90 or score > 80:
    print("B")
elif score > 60:
    print("C")
else:
    print("D")
    
# R: B
    
#=============Pergunta 4:

#What will be printed in the console?

def a_function(a_parameter):    
    a_variable = 15    
    return a_parameter 
a_function(10)
print(a_variable)

# R:NameError

#=============Pergunta 5:

#What will be printed as the output?

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

# R:15

#=============Pergunta 6:

#Given a Car Class has the following attributes and methods, which line of code in the answers will produce an error?
#Attributes:
#num_of_seats
#speed
#Methods:
#drive()
#break()

# R: car.break = 0

#my_toyota = Car()
#my_fiat = Car()
#What word would you use to describe my_toyota and my_fiat?

# R: Object

#=============Pergunta 7:

#If you are writing code inside the main.py file to open the quiz.txt what would be the relative file path?

# R:"quiz.txt"

#=============Pergunta 8:
#What is the output of this code?

def foo(a, b=4, c=6):
    print(a, b, c)
 
foo(20, c=12)

#R: 20 4 12

#=============Pergunta 9:

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)

#R: 4 (7, 3, 0) {'x': 10, 'y':64}

#=============Pergunta 10:
#What's the print output for the following code? You do not need a computer to calculate this.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)

# R: [5, 11, 17]