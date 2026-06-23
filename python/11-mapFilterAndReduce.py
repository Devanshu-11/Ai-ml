# Map- It applies a function to every time in an iterable
numbers=[1,2,3,4,5,6,7,8];
squared=list(map(lambda x:x**2, numbers));
print(squared);

# Filter- It selects the element that satisfy a condition
numbers=[1,2,3,4,5,6,7,8];
evens=list(filter(lambda x:x%2==0, numbers));
print(evens);

# Reduce- It Reduces an iterable to a single value by repeatedly applying a function
from functools import reduce
numbers=[1,2,3,4,5,6,7,8];

# a is accumulator and b is current item
total=reduce(lambda a,b: a+b,numbers,0); # 0-to define the initial value
print(total);