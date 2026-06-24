# Error Handling allows a program to continue running or fail gracefully when unexpected errors occur,It uses try,except,else and finally blocks for exception handling

# 1-Basic syntax
try:
    a=int(input("Enter a number: "));
    b=int(input("Enter a number: "));
    result=a/b;
except ValueError:
    print("Please enter a valid integer");
except ZeroDivisionError:
    print("Cannot divide by zero");
else:
    print("The result is:",result); # it will run if no exception occurs
finally:
    print("Program ended"); # this block will always executes, whether an exception occurs or not

# 2-Raising Exception-we can create own exception using raise
age=int(input("Enter the age: "));
if(age<18):
    raise ValueError("Age must be 18 or above");
print(age);

# 3-Custom Exception
class InsufficientBalanceError(Exception):
    pass # pass means that initially do nothing

balance=1500;
withdraw=int(input("Enter the Withdraw Amount: "));

if(withdraw>balance):
    raise InsufficientBalanceError("Not enough balance");