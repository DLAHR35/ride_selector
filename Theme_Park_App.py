#From the book Begin to Code with Python
#This app allows a user to select a ride and input their age to determine if they meet the age requirement for riding.

print('''Welcome to the ride information station! 

We currently offer the following rides:

1 - Scenic River Cruise
2 - Carnival Carousel
3 - Jungle Adventure Water Splash
4 - Downhill Mountain Run
5 - The Regurgitator
''') #This prints the menu to inform the user of the available rides

#input that ask for the user to select the ride they wish to ride. This feeds into the if statement
ride_selection = input("Please enter the ride number you wish to ride: ")
ride_selection_int = int(ride_selection)

if ride_selection_int == 1: #IF statement that determines what path to take based on the user's input.
    print("\nYou have selected the Scenic River Cruise.")
    print("There is no age limit for this ride. You may ride this ride.")

elif ride_selection_int >1 and ride_selection_int <6:#Selecting numbers 2 - 5 prompts the user to enter their age because of age restrictions
    rider_age = int(input("\nPlease enter your age in years (0 - 100): "))
    
    #the following if statements determines and informs the rider if they are within the age limits of each ride.
    if ride_selection_int == 2:
        print("\nYou have selected the Carnival Carousel.")
        if rider_age >=3:
            print("You are old enough to ride. Please enjoy!")
        else:
            print("We are sorry, you are too young for this ride.")
    
    if ride_selection_int == 3:
        print("\nYou have selected the Jungle Adventure Water Splash.")
        if rider_age >=6:
            print("You are old enough to ride. Please enjoy!")
        else:
            print("We are sorry, you are too young for this ride.")
            
    if ride_selection_int == 4:
        print("\nYou have selected the Downhill Mountain Run.")
        if rider_age >=9:
            print("You are old enough to ride. Please enjoy!")
        else:
            print("We are sorry, you are too young for this ride.")
 
    #This if statemet determines if the rider is too young or too old, and provides output based on their age.
    if ride_selection_int == 5:
        print("\nYou have selected the Regurgitator.")
        if rider_age >=12 and rider_age <=70:
            print("You are old enough to ride. Please enjoy!")
        elif rider_age >70:
            print("Due to the aggresive nature of this ride, we can not allow you to ride. We apologize for the inconvienence.")
        else:
            print("We are sorry, you are too young for this ride.")

