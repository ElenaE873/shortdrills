from random import choice
#to get a random question from a list
# "random choice function" needs to be imported from the random library
# if you do not import choice then you must use random.choice(), but if it is imported it can just be used as choice()


questions = ["Why is python so great?: ", "Why do we use Python?: ",
                     "what's so special about python?: ", "But why?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("Oh... Okay")
    
