# Dictionary is a built-in data structure which stores the data in key-value pairs, in this values can be duplicate but the key should be unique

# 1-Creating the dictionary
student={
    "name":"Devanshu Kansal",
    "age":34,
    "course":"B.Tech"
};

# 2-To access the value
print(student["name"]);
print(student["age"]);
print(student["course"]);

# Here we can also use get keyword
print(student.get("name"));
print(student.get("city", "Not Found")); # we can also add the default values

# 3-Adding the new item
student["city"]="Delhi";
print(student);

# 4-To update the value
student.update({"age":24});
print(student);

# 5-To delete the value
student.pop("age");
print(student);

del student["city"];
print(student);

# 6-To access the key
for key in student:
    print(key);

# 7-To access the value
for value in student.values():
    print(value);

# 8-Print both key and value pair
for key, value in student.items():
    print(key,":",value);