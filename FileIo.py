# Author: Liam Hugo Kennon
# Date: 12/1/23
# Description: Controls data within a file
# Challenges: N/A
# Bugs: N/A
# None

def main():
   
    """ doc """
    file_input = open("C:/Users/lkennon26/Desktop/gcds_data3.csv") #gives a file to read

    file_input.readline()                                          #skip first line of header info
    answer = "Y"
    go = True

    #Choice board(what do you want to do?)


    print("Menu: Enter Choice or 'Q' to (Q)uit:")
    print("1) Print All Student in Grade 12")
    print("2) Compare number of males to females")
    print("3) Print all students living in CT")
    print("4) Print specific student")
    print("5) Print number of the same first names")
    print("6) Add new record")



    while go is True:

        #Main function

        if answer == "1":
            check_seniors(file_input)
        elif answer == "2":
            type_of_gender = input("Which gender would you like to find?")
            male_female(file_input, type_of_gender)
        elif answer == "3": 
            check_state(file_input)
        elif answer == "4":
            find_person(file_input)
        elif answer == "5":
            count_first(file_input) 
        elif answer == "6":
            add_person(file_input)   
        elif answer == "Q":
            go = False
            print("bye")
            return
           
        answer = input("Enter Choice or 'Q' to quit")


def check_seniors(file):
    #Finds amount of students in 12th grade
    #takes in the the number choice from the user
    #returns all the seniors     
    """ doc """
    file.seek(1)                                     #move pointer to line 1

    for record in file:
        attribute = record.split(",")
        if attribute[2] == "Grade 12":
            print(attribute[0] + " " + attribute[1])

def male_female(file, type_of_gender):
    #counts number of males and females and gives the percentage
    #takes in number of males and females
    #returns the percentage of the two
    """ doc """
    file.seek(1)                                     
    count_1 = 0
    count_2 = 0
    for record in file:
        attribute = record.split(",")
        count_1 += 1
        if attribute[3] == type_of_gender:
            count_2 += 1
    percentage = round((count_2/count_1) * 100)
    print(f"{percentage}% of the school is {type_of_gender}")

    
  

def check_state(file):
    #finds number of people living in CT
    #takes in the state attribute 
    #returns number of people in the state
    """ doc """
    file.seek(1) 
    for record in file:
        attribute = record.split(",")
        state = attribute[6]
        print(state)
        if state[0:2] == "CT":
            print(attribute[0] + " " + attribute[1]) 

def find_person(file):
    #finds a specific file in the file
    #takes in first and last names 
    #returns the complete file
    """ doc """
    file.seek(1) 

    user_last = input("enter last name")
    user_first = input("enter first name")
   

    for record in file:                                         #iterate through file
        attribute = record.split(",")                           #store one record at a time
        last_name = attribute[0]                                #take last name from record
        first_name = attribute[1]                               #take first name from record
        if first_name == user_first and last_name == user_last: 
            print(attribute[0] + " ," + attribute[1] + " ," + attribute[2] + " ," + attribute[3] + " ," + attribute[4] + " ," + attribute[5] + " ," + attribute[6]) 

def count_first(file):
    #counts the number of people with the same first name and says how many of those first names exist
    #takes in a first name
    #returns amount of the number of people with the name and the name
    """ doc """
    first_name = input("enter first name")
    counter = 0
    file.seek(1)                                     #move pointer to line 1

    for record in file:
        attribute = record.split(",")
        if attribute[1] == first_name:
             counter +=1
        
    if counter == 0:
        print("NOT FOUND")
    else: 
        print(f"{counter}, {first_name}s")
        

def add_person(file):
    #adds a record to the file
    #takes in the attributes in each indivdual column
    #returns a new record added to the file
    """ doc """
    for record in file:
        attribute = record.split(",")   

    add_first_name = input ("enter new first name")
    add_last_name = input ("enter new last name")
    add_grade = input ("enter student grade")
    add_gender = input ("enter student gender")
    add_address = input ("enter student address")
    add_city = input ("enter student city")
    add_state = input ("enter student state")
    
    file.close()                                                                                                                                   #close the file
    file = open("C:/Users/lkennon26/Desktop/gcds_data3.csv", "a")                                                                                  #open the file
    file.write((add_last_name + "," + add_first_name + "," + add_grade + "," + add_gender + "," + add_address + "," + add_city + "," + add_state)) #taking user data and compartmentalizing it
    file.write("\n")                                                                                                                               #open as an append file
    file.close()                                                                                                                                   #close the file 
    file = open("C:/Users/lkennon26/Desktop/gcds_data3.csv")                                                                                       #open as a read file


       

if __name__ == '__main__':
    main()
