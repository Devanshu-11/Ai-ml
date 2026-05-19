# Data types define the kind of value a variable can hold, python is a dynamically typed, so we don’t need to declare the type explicitly

# 1-Numeric Types-int,float 
x=10;
y=3.14;

# 2-Sequence Types- Str,list,tuple
name="Devanshu Kansal";

# List- Ordered Mutable collection- we can add,delete or modify the value
fruits=["apple","banana","cherry"];
print(fruits[0], fruits[1], fruits[2]);
data = [3.14,"Devanshu Kansal",123]

# Tuple- Ordered Immutable collection- we cannot add,delete or modify the value
point=(10,20);
print(point);

# 3-Set- Unordered collection of unique elements and it is mutable set and frozenset-immutable set
numbers={1,2,3};
frozen=frozenset([1,2,3]);

# 4-Mapping Type- Dictionary-Stores data in key–value pairs
student={"name":"John","age":20};

# 5-Boolean Type- Stores True or False values 
is_valid=True;
print("Is value is valid:",is_valid);

# 6-Binary Types- It is used to store the Binary data 
b=b"hello";

# 7-None Type-It represents the absence of value 
x=None;