######-------------------code-----------------------------------------------------
starting_phrase = input("Please enter a sentence: ").strip().lower()

words = starting_phrase.split()

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
            
output_phrase = " ".join(new_words) 
print(output_phrase)
#####------------------run-through------------------------------------------------------

# -- Ask user for input, a phrase to build on with the loop:
starting_phrase = input("Please enter a sentence: ").strip().lower()

# -- Need to break out the sentence into individual pieces
words = starting_phrase.split()
print(words)

#  -- Once the pieces of the sentence are iterables, we loop through words and convert it into the language we want
#  -- Below i've chosen to a version of pig latin.

new_words = [] #must begin from scratch, onto which to build a list that will be the outcome of the loop
# -- this is absolutely necessary for building a new output of the loop

for word in words:  #for every iterable in the list of words
    #words is the variable where we split each work in the sentence as iterables

# -- if the first letter is a vowel then add 'tay' to the end of the word
    if word[0] in "aeiou": 
        new_word = word + "tay"
        new_words.append(new_word) #adding the new word in the list we're building new_words

    # -- if the first condition is False, we need to keep track of the positions as we loop through.
    else:
        vowel_pos = 0  #vowel position is equal to zero where the condition was False

        # -- if that letter is not a vowel then we need to increment that vowel position by 1 as we move through loop
        for letter in word:  # letter here is the iterable in the iterables of word which we already said above is the iterable of words
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1

                # -- if it is a vowel, then we need it to stop because that's where our consonants end
            else:
                break

        # -- building the new
        cons = word[:vowel_pos]
        #the consonants are anything form the beginning of the workd to vowel position.

        the_rest = word[vowel_pos:]
        #anything else is from the vowel position to the end of the word.

        new_word = the_rest + cons + "ayt"
        new_words.append(new_word)
        #new sentence elements or words
                
# -- Join the words together in a new sentence phrase
output_phrase = " ".join(new_words) 
print(output_phrase)
