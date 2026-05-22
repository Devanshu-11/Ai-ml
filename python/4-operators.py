# 1-Arithmetic Operators
a=10;
b=3;
print(a+b);

# Floor division
print(a//b); 
print(a/b);

# 2-Comparison Operators
a=5;
b=10;
print(a==b);
print(a!=b);

# 3-Logical Operators
x=5;
print(x>2 and x<10);

# 4-Membership Operators- check if the value is present in collection or not
nums=[1,2,3];

print(2 in nums);
print(5 not in nums);

# 5-Bitwise Operators
a=5 # 101 
b=3 # 011
print(a&b); # if both are 1 then 1
print(a|b); # if either of them is 1
print(a^b); # if both have different bits

# ~a=-(a+1)
print(~a);
print(a<<1) # Left shift
print(a>>1) # Right shift