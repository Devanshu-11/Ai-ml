# In python,Regular expressions(Regex) are handled using the in-built re functions
import re;

# 1-re.search()-It basically finds the first match and then it stops
text="My number is 12 34 56 78";

# r"\d+" means look for the first continuous block of numbers
match=re.search(r"\d+",text);
if match:
    print(match.group()); # output-12

# 2-re.findall()-To find all the matches in the entire string
match=re.findall(r"\d+",text);
print(match); # output-['12','34','56','78']

# 3-re.match()-checks for a match only at the beginning of the string
text="Hello World";
match=re.match(r"World",text);
print(bool(match)); # output-false

match=re.match(r"Hello",text);
print(bool(match)); # output-true

# 4-re.sub()-it replaces all matched patterns
text="Price is $200 $100 $50 $100";
result=re.sub(r"\d+","200",text);
print(result); # output-Price is $200 $200 $200 $200