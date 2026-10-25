# to read entire file and it stores entire file in a single string
file=open("file.txt","r");
content=file.read();
print(content);
file.close();

# read one line
file=open("file.txt","r");
print(file.readline());
file.close();

# read all lines and it stores each line in a lists of string
file=open("file.txt","r");
lines=file.readlines();
print(lines);
file.close();

# Writing to a file- it completely overwrites with a text
file=open("file.txt","w");
file.write("I am writing a new line");
file.close();

# append in a file-it does not destroying the old data,instead add data to last line
file=open("file.txt","a");
file.write("\nWelcome to file handling");
file.close();

# check if file exists or not
import os;

if os.path.exists("file.txt"):
    print("File exists");
else:
    print("File does not exist");