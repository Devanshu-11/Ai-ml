# Conditionals are used to make decisions in code

# 1-if statement
x=10;
if x>=10:
    print("Age is greater than 10");

# 2-if-else Statement
x=10;
if x>=18:
    print("Adult");
else:
    print("Minor");

# 3-if-elif-else Statement
marks=65;
if marks>=80:
    print("A+");
elif marks>=60:
    print("A");
elif marks>=40:
    print("B+");
else:
    print("Fail");

# 4-Nested if
age=20;
has_id=True;

if age>=20:
    if has_id==True:
        print("Entry allowed");

# 5-Multiple Conditions using and
age=22;
is_Citizen=True;
if age>=22 and is_Citizen:
    print("He is eligible to vote");
else:
    print("He is not eligible to vote");

# 6-Multiple Conditions using or
day="Sunday";
if day=="Saturday" or day=="Sunday":
    print("You can go to play");

# 7-not Operator
is_raining=False;

if not is_raining:
    print("Go outside");