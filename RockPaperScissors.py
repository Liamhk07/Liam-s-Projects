
import random

possible_actions = ["rock", "paper", "scissors"]
valid_user_responses = ["rock", "paper", "scissors", "stop", "quit"]

p_score = 0
c_score = 0

while True:
    user_action = input("Type stop or quit to end. Rock, paper, or scissors?: ")
    computer_action = random.choice(possible_actions)

    if user_action not in valid_user_responses:
        print("invalid")

    else:
        if user_action == "stop" or user_action == "quit":
            print("Game over! Bye")
            break

        print("You chose: " + user_action + " Computer chose: " + computer_action)

        if user_action == computer_action:
            print("It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock beats scissors you win")
                p_score += 1
            elif computer_action == "paper":
                print("Paper beats rock you lose.")
                c_score += 1
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper beats rock you win")
                p_score += 1
            elif computer_action == "scissors":
                print("Scissors cuts paper you lose.")
                c_score += 1
        elif user_action == "scissors":
            if computer_action == "paper":  
                print("Scissors beats paper you win")
                p_score += 1
            elif computer_action == "rock":
                print("Rock beats scissors you lose.")
                c_score += 1
        
        print("Score is: You - " + str(p_score) + " Computer - " + str(c_score))






