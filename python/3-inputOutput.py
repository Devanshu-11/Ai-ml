# input() always takes data as a string
name=input("Enter your name: ");
print(name);

# to converting input to other types and in case,we define int,we can only put integer values not other than that like-float or any other
ageInt=int(input("Enter your age in int: ")); 
print(ageInt);

ageFloat=float(input("Enter your age in float: "));
print(ageFloat);

# In case of multiple inputs
a,b=input("Enter 2 numbers: ").split();
a=int(a);
b=int(b);
print("The value of a is: ",a,"and b is: ",b);