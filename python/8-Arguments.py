# 1-Positional Arguments
def intro(name,number):
    print('The name is:',name);
    print('The number is:',number);

intro('Devanshu',22);

# 2-Default Argument
def greet(name="Guest"):
    print("Hello",name);

greet();
greet('Devanshu Kansal');

# 3-Variable Arguments-To handle the unknown values
def numbers(*nums):
    print(nums);

numbers(1,2,3,4,5);

# 4-Keyword Arguments-
def introKey(name,age):
    print(name,age);

introKey(name='Devanshu Kansal',age=34);