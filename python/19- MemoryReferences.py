# In python,variables do not store the objects directly instead they store references to objects in memory

x=[1,2,3];
y=x; # here y is the same reference
print(x); # output-[1,2,3]
print(y); # output-[1,2,3]

# append the value to it
y.append(4);

print(x); # output-[1,2,3,4]
print(y); # output-[1,2,3,4]

# checking the id
print("The id of x is:",id(x));
print("The id of y is:",id(y));

# to make different copy
a=[1,2,3];
b=a.copy();
print(a); # output-[1,2,3]
print(b); # output-[1,2,3]

#a append the value to it
b.append(4);

print(a); # output-[1,2,3]
print(b); # output-[1,2,3,4

# checking the id
print("The id of a is:",id(a));
print("The id of b is:",id(b));