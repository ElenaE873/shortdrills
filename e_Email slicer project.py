#get user email address

email= input ("what is your email address?: ").strip() # strip away all blank spaces


#slice out user name
#everything up to the @symbol
#take an index slice of the email up to the @symbol

user = email[:email.index("@")]
#using a variable user to assign it an email slice of the email variable input from user up until the @symbol


#slice out domain name

domain = email [email.index("@") + 1 :]
#start is the @symbol but you want to start at one after it and then all the way to the end

#format message
output = "Your username is {} and your domain name is{} ".format(user,domain)


#display output message
print(output)
