# List is a Ordered Mutable collection of items in which we can insert,update or delete the items

# 1-Creating a list
fruits=["banana","apples","orange"];
numbers=[1,2,3,4,5];
mixed=[1,"hello",3.14,True];

# 2-Accessing the elements
print(fruits[-2]); # fetching the last 2nd item

# 3-Modifying the elements
fruits[1]="mango";
print(fruits);

# 4-Adding the elements
fruits.append("grape"); # Add to last index
fruits.insert(1,"Kiwi"); # insert to index-1
print(fruits);

# 5-Removing the elements
fruits.remove("banana"); # Remove by value
fruits.pop(); # Remove last item
del fruits[0]; # Remove by index
print(fruits);

# 6-List slicing
numbers=[1,2,3,4,5,6,7,8];
print(numbers[1:4]); # 2,3,4, here from start index to end index-1
print(numbers[:4]); #1,2,3,4, here 0th index to end index-1
print(numbers[4:]); #5,6,7,8, here 4th index to end index-1 

# 7-iterate through lists
numbers=[1,2,3,4,5,6,7,8];
for number in numbers:
    print(number);

# 8-Other methods
numbers.sort()      # Sort list
numbers.reverse()   # Reverse list
print(len(numbers)) # Length
print(max(numbers)) # Largest value
print(min(numbers)) # Smallest value