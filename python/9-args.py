# *args—collects extra positional arguments into a tuple and it means i can took as many as arguments as i want
def greet(*args):
    for name in args:
        print(f"Hello, {name}");

greet("Alice", "Bob", "Charlie");

# **kwargs-collects extra keyword arguments into a dictionary and it lets us to pass the key value pairs like dictionary
def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}");

display_info(name="Alice",age=25,city="London");

# In this, i am both using the *args and **kwargs
def both_display(*args,**kwargs):
    print("Positional:",args);
    print("Keyword:",kwargs);

both_display(1,2,3,name="Alice",age=25);