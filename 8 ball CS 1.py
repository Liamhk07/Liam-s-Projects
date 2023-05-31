# Author: Liam Kennon
# Date: 3/2/23
# Description: Takes any question asked and gives a random response picked from a list of options
# Challenges: N/A
# Bugs: N/A
# None

import random # Brings in a library called random, which includes different functions to randomize

responses = ["Yes", "No", "Maybe", "Ask again later"] # creates a list of responses for the magic 8 bal

while True: # Enters a forever loop
    question = input("Ask me a question") # Prompts the user to enter a question and stores their response as the variable question
    if question.lower() == "stop": # If the user enters stop
        break #then break the loop, effectively ending the program
    print(random.choice(responses)) # Print a random option from the list of magic 8 ball responses
