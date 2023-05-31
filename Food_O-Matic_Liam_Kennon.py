#Author: Liam Kennon
#Date:4/5/23
#Description: 
#Challenges: Change the domain to a pasta resturant
#Bugs:N/A

import random#Import the random library
import sys
pastas = ["fettucini", "bow tie", "linguini", "shell", "Angel Hair Pasta", "Bow Tie Pasta", "Bucatini Pasta", "Ditalini Pasta", "Egg Noodles", "Fusilli Pasta"]#List of the pastas on the Menu
sauces = ["alfredo", "bolognese", "carbonara", "pesto", "Hot Sauce", "Barbecue Sauce", "Horseradish Sauce", "Soy Sauce", "Tartar Sauce", "Taco Sauce"]         #List of sauces for the pastas
seasonings = ["truffle", "pepper", "salt", "red chili flakes", "cinnamon", "cumin", "dill", "saffron", "nutmeg", "mustard"]                                    #List of seasonings for the pasta
prices = ["$10", "$20", "$13", "$11", "$21", "$19", "$14", "$18", "$32", "$3"]                                                                                 #List of the prices of the pasta combos

while True:                                                     #While the following is true
    answer = input ("Do you want some food? ")                  #The input is equal to the answer the customer gives

    if answer == "yes":                                         #If the customer answeres yes 
        break                                                   #stop program
    elif answer == "we are not eating":                         #If the customer answers we are not eating 
        print ("Sounds good, have a nice day")                  #Robot prints sounds good, have a nice day   
        sys.exit()                                              #Stop running the program
    else:                                                       #if the answer is not equalm to the base answers
        print("Invalid")                                        #print invalid

while True:                                                     #While the following applies
    items = input("How many items do you want? ")               #Robot asks how many items the customer wants
    
    if items.isnumeric():                                       #check that items is a number
         for item in range(int(items)):                         #iterate through all indexes in each list
            pastas = random.choice(pastas)
            print(f"{pastas}  {random.choice(sauces)}  {random.choice(seasonings)} {random.choice(prices)}") #Choose a random item from the menu/list
    
    else:                                                       #other then that
        print("Enter a number")                                 #robot asks for the customer to enter a number