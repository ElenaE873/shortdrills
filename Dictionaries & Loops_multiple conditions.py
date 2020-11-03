films = {#This is a dictionary of movies, each with it's own list of age and num_seats
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters":[12, 5]
    }

while True:

    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films: #meaning if the answer to the question is found in the films dictionary list
        age = int(input("How old are you?: ").strip())
         #casting (w/"in") from string to an interger (making sure you strip away any spaces from the answer)
        #you end up casting to interger because the input function always brings in a string
        #then proceed with the next question

        # check user age

        if age >= films[choice][0]:
            #the film choice is then put through the dictionary to give us the age threshold for that movie, index 0 is the age element of that list
            # and if that is true,
            #then 
            #the code checks for the threshold of the number of seats

            # check enough seats

            num_seats = films[choice][1]
             #and if the number of seats in the dictionary is greater or equal to zero, it proceeds to let the user know to "Enjoy the Film!"
            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1 #overriding the number of seats back and saving it with each response
            else:
                print("Sorry, we are sold out!") #the loop will run to the end until (-1) will eliminate the number of seats
        else:
            print("You are too young to see that film!") #the loop will second to last check for age
    else:
        print("We don't have that film...") #the loop will first check if the film is in the list
    
#the indentation alignment matters as the loops the inward, the output moves outward.
