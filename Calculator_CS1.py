#Author: Liam Kennon
#Date: 5/15/23
#Description: Basic calculator that can add, subtract, multiply and divide integers
#Challenges:
#Bugs: N/A

def check_int():#defining check int
    while True:#While this is true 
        num = input("Enter an integer: ")#setting num equal to input
        
        try:
            return int(num)  # Try to convert the input to an integer and return it
        except ValueError:
            print("Please enter an integer!")  # Display an error message if the input is not a valid integer

def add(a, b):
    print(a + b)  # Print the sum of the two numbers
def sub(a, b):
    return a - b  # Return the difference between the two numbers
def mult():
    a = check_int()  # Prompt the user to enter the first integer
    b = check_int()  # Prompt the user to enter the second integer
    return a * b  # Return the product of the two numbers
def div():
    a = check_int()  # Prompt the user to enter the first integer
    b = check_int()  # Prompt the user to enter the second integer
    return a / b  # Return the division of the two numbers
def sum(numbers):
    total = 0  # Initialize the total variable to zero
    
    for number in numbers:
        total += number  # Add each number in the list to the total
    
    return total  # Return the sum of the numbers
def main():#Defining main
    print("Which form of calculation.")#Ask which form they want
    print("1.Add")#add
    print("2.Subtract")#subtract
    print("3.Multiply")#multiply
    print("4.Divide")#divide
    
while True:#while this is true
        entry = input("Enter choice (1/2/3/4): ")  # Prompt the user to enter a choice
        
        if entry == '1':#If entry is 1
            a = check_int()  # Prompt the user to enter the first integer
            b = check_int()  # Prompt the user to enter the second integer
            add(a, b)  # Call the add function with the entered integers
        elif entry == '2':#if entry is 2
            a = check_int()  # Prompt the user to enter the first integer
            b = check_int()  # Prompt the user to enter the second integer
            print(sub(a, b))  # Print the difference between the entered integers
        elif entry == '3':#if entry is 3
            print(mult())  # Call the mult function and print the result
        elif entry == '4':#If entry is 4
            print(div())  # Call the div function and print the result
        elif entry == '5':#If entry is 5
            numbers = []  # Create an empty list for numbers
            
            while True:#While this is true
                num = input("Enter 'stop' to quit entering numbers and get sum: ")  # Prompt the user to enter a number or 'stop'
                
                if num == "stop":#If the input is stop
                    break  # Exit the inner loop if 'stop' is entered
                else:#Otherwise
                    num = check_int()  # Convert the entered value to an integer
                    numbers.append(num)  # Add the number to the list
                    
            print(sum(numbers))  # Calculate the sum of the numbers in the list and print it
        elif entry == '6':#if entry is 6
            break  # Exit the outer loop if '6' is entered
        else:#Otherwise
            print("Invalid")  # Display an error message for an invalid choice