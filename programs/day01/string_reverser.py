word = input("Please enter a word to reverse: ")
if word == "":
    print ("please enter a valid word to reverse: ")
else:
    reverse_word = word [: :-1]
    print (f"the reverse of word {word} is : {reverse_word}")