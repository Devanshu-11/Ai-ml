# Function is a reusable block of code that performs a specific task and we define a function using the def keyword

# Method-1-To define a function
def greet():
    print('Hello');

greet();

# Method-2-When we passing an argument
def greetFun(name):
    print('The name is:',name);

greetFun('Devanshu Kansal');

# Method-3-Function with a return value
def add(a,b):
    return a+b;

result=add(3,4);
print('The result of addition is:',result);

# Method-4-Default Parameters
def defaultGreet(name="Guest"):
    print("The name is:",name);

defaultGreet();
defaultGreet('Devanshu Kansal');