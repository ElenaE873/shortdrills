#putting pieces of string together

#- 1 - Ask user for name.
name = input ("What is your name?: ")
print(name)

#- 2 - Ask user for age.
age = input ("What is your age?: ")
print(age)

#- 3 - Ask user where they live.
city = input ("What city do you live in?: ")

#- 4 - Ask user what they enjoy!
love = input ("What do you love doing?: ")

#- 5 - Create output text.
string= "Your name is {} and you are {} years old.  You live in {} and you love {}."
output = string.format(name, age, city, love)

#- 6 - Print output to the screen.
print(output)
