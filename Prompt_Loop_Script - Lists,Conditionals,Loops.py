greatest_women_inscience = ["AdaLovelace", "MarieCurie", "JanakiAmmal", "ChienShiungWu", "RosalindFranklin", "VeraRubin", "JenniferDoudna", "FlossieWongStaal"]

size=(len(greatest_women_inscience))

while True: #a while loop that will make whatever is typed inside of the loop run over and over
    print("Hi! I am list of incredible women in science.")
    guess = input("Guess which incredible women in science might be on this list (hint:first and second names only, no spaces, first letter always capitalized, ex - AdaLovelace: "
                  ).strip().format(size)
    '''a user input will be required for the question mentioend in parantheses,
    and that answer will be stored in the variable called "guess"'''

    if guess in greatest_women_inscience:
        print("Your answer {} in on the list!".format(guess))
        checkpoint_1 = input("Would you like to stop here?: ").strip().lower()
        
        if checkpoint_1 == "y":
           greatest_women_inscience.remove(guess)
        elif checkpoint_1 == "n":
            print("No problem, let's try again!")
            
    else:
        print("Hmmm I don't think you are getting the {} correctly".format(guess))
        add_me = input("However, if you believe this is a woman in science that should be on this incredible list, we can add it, which name is it you'd like to add?: ").strip().lower()
        if add_me == "y":
             greatest_women_inscience.append(guess)
        elif add_me == "n":
            print("No worries, see you around!")
            break
