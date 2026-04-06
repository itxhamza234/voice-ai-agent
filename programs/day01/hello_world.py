# my First program in pyhton
print ("Hello, I am starting the learning 30-Day AI Engineer Roadmap.")


# Variables and datatypes
name = "Amer Hamza"
age = 25
is_Student = True
Marks = 2.6
print (f"My name is {name}, My age is {age}, I am {is_Student}, My marks are {Marks}.")
print (f"Type of name: {type(name)}, Type of age: {type(age)}. type of is_Student: {type(is_Student)}, type of marks: {type(Marks)}.")

# Strings

name = "Ameer Hamza"
print (f"length of name characters: {len(name)}, Uppercase: {name.upper()}, Lowercase: {name.lower()}, First character: {name[0]}, First five characters: {name[0:5]}")

# Slice the string
first_name = "Ameer"
Second_name = "hamza"
full = first_name + " " + Second_name
print (full)

# f_string

print (f"My name is {full}, I am learning python programming language.")

# input/output


name = input("Please input your name: ")
age = int(input("please input your age: "))
print (f"Hello {name},your age is {age}, next year you will be {age + 1}.")

