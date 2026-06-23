# It is ordered immutable collection of data items, here we cannot modify,add or delete the elements into it

# 1-Creating the tuple
t1=(); # initialize the empty tuple
t2=(1,2,3); # tuple with values
t3= (5,); # single element tuple but seperated with comma

# 2- Tuple Operations
t4=(1,2,3,4,5);
t5=(6,7,8);
print(t4+t5); # it concats it
print(t4*2); # it just makes the repitition
print(len(t4)); # to find the length

# 3-In Tuples,we can do packing and unpacking
# Packing
person=("John",32,"Engineer");

# Unpacking
name,age,job=person;
print("The name is:",name);
print("The Age is:",age);