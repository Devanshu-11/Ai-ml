# Set is a Unordered Mutable collection of items in which we can insert,update or delete the items and in set,i can also do union,intersection and difference and it only adds the unique elements into it and immutable version of set is frozen set

# 1-Creating a set
fruits={"apples","banana","mangoes"}; # by using curly braces
numbers=([1,2,3,4]); # by using set

# 2-Adding the elements
fruits.add("orange"); # it adds element to the last
fruits.update(["grape", "mangoes"]); # to add the multiple elements
print(fruits);

# 3-To remove elements
fruits.remove("banana"); # Raises error if not found
print(fruits);

fruits.discard("apples"); # No error if not found
print(fruits);

removed=fruits.pop(); # Removes a random element as it is unordered so there is no concept of first and last element
print(fruits);

fruits.clear(); # Removes all elements
print(fruits);

# Other methods
A={1,2,3};
B={3,4,5};

# Output-{1,2,3,4,5}
print(A|B); # for union

# Output-{3}
print(A&B) # for Intersection

# Output-{1,2}
print(A-B) # for difference

# Output-{1,2,4,5}
print(A^B) # for symmetric difference- it does not includes common

# Membership testing
nums={10,20,30};
print(20 in nums);
print(50 in nums);