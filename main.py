import random

# (5 points): As a developer, I want to make at least three commits with descriptive messages.
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, 
        # and entertainment selections in their own separate lists.
# (5 points): As a user, I want a destination to be randomly selected for my day trip.

##################################################################################################################################

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

##################################################################################################################################

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode 
        # of transportation, and/or form of entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all 
        # of the random selections.
# (10 points): As a user, I want to display my completed trip in the console.

##################################################################################################################################

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, 
#       each function should do just one thing!
##################################################################################################################################

destinations = ["Canada", "Spain", "Tokyo", "London", "Fiji Island"]
restaurants = random.choice(["Noma", "Geranium", "Asador Etxebarri", "Disfrutar Frantzén"])
transportation_selections = random.choice(["Rolls-Royce Phantom", "Bugatti Chiron", "Private Jet", "Public Plane", "Helicopter"])
entertainment_selections = random.choice(["Skydiving", "Concert", "Mountain Climbing", "Space Walk", "Escape Island"])

def trip_destination(places):
    places = random.choice(places)
    return places


def trip_restaurants(foods):
    foods = random.choice(foods)
    return foods


def trip_tranportation(cars):
    cars = random.choice(cars)
    return cars


def trip_entertainment(activities):
    activities = random.choice(activities)
    return activities


def destination_choice(answer):
    invalid = True
    while invalid == True:
        choice = input("Would you like this trip? (Y/N) ")
        if choice == "Y" or choice == "y":
            print("Have a safe Trip! (^_^) ")
            answer = False
            invalid = False
        elif choice == "N" or choice == "n":
            print("Let Us please reselect this for you. ")
            answer = True
            invalid = False
        elif choice != "Y" or choice != "y" or choice != "N" or choice != "n":
            print("Invalid choice please try again! ")
            answer = True
            invalid = True
    return answer


def transportation_choice(cont):
    invalid = True
    while invalid == True:
        choice = input("Do you wish to change your mode of transportation? (Y/N) ")
        if choice == "Y" or choice == "y":
            print("Happy travels! (^_^) ")
            print()
            answer = False
            invalid = False
        elif choice == "N" or choice == "n":
            print("Let Us please reselect this for you. ")
            print()
            answer = True
            invalid = False
        elif choice != "Y" or choice != "y" or choice != "N" or choice != "n":
            print("Invalid choice please try again! ")
            print()
            answer = True
            invalid = True
    return answer




def restaurants_choice(answer):
    invalid = True
    while invalid == True:
        choice = input("Would you like another choice? (Y/N) ")
        if choice == "Y" or choice == "y":
            print("This is a great choice (^_^) ")
            answer = False
            invalid = False
        elif choice == "N" or choice == "n":
            print("Let Us please reselect this for you. ")
            answer = True
            invalid = False
        elif choice != "Y" or choice != "y" or choice != "N" or choice != "n":
            print("Invalid choice please try again! ")
            answer = True
            invalid = True
    return answer





def entertainment_choice(answer):
    invalid = True
    while invalid == True:
        choice = input("Would like to change your entertainment (Y/N) ")
        if choice == "Y" or choice == "y":
            print("Have a safe Trip! (^_^) ")
            answer = False
            invalid = False
        elif choice == "N" or choice == "n":
            print("Let Us please reselect this for you. ")
            answer = True
            invalid = False
        elif choice != "Y" or choice != "y" or choice != "N" or choice != "n":
            print("Invalid choice please try again! ")
            answer = True
            invalid = True
    return answer







cont = True
while cont == True:
    print()
    trip_location = trip_destination(destinations)
    print("Your destination is",trip_location )
    cont = destination_choice(cont)

cont = True
while cont == True:
    print()
    trip_ride = trip_tranportation(transportation_selections)
    print("Your destination is",trip_ride)
    cont = transportation_choice(cont)

cont = True
while cont == True:
    print()
    trip_food = trip_restaurants(restaurants)
    print("Your destination is",trip_location )
    cont = restaurants_choice(cont)

cont = True
while cont == True:
    print()
    trip_fun = trip_entertainment(entertainment_selections)
    print("Your destination is",trip_location )
    cont = entertainment_choice(cont)



print("Have fun with your", trip_fun, "staying in" , trip_location , "while driving a", trip_ride, "and dining at",trip_food)
        

















