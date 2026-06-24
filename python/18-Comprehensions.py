# Comprehensions is a concise way to create collections(list,tuples and dictionaries) from the existing iterables

# 1-List Comprehension
square=[x*x for x in range(5)];
print(square);

# if i write with a condition
square=[x*x for x in range (1,12) if x%2==0];
print(square);

# 2-Dictionary Comprehension
square={x:x*x for x in range(5)};
print(square);

# 3-Set Comprehension
unique_lengths={len(word) for word in ["apple","cat","banana"]};
print(unique_lengths);

# 4-Nested Comprehension
matrix=[[1, 2],[3, 4],[5, 6]];
flat=[num for row in matrix for num in row];
print(flat);

# others
fruits=["apples","banana","mangoes"];
print(len(fruits));