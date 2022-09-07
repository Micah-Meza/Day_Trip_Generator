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

cont = True
destinations = ["Canada", "Spain", "Tokyo", "London", "Fiji Island"]
restaurants = random.choice(["Noma", "Geranium", "Asador Etxebarri", "Disfrutar Frantzén"])
transportation_selections = random.choice(["Rolls-Royce Phantom", "Bugatti Chiron", "SSC Tuatara", "BMW i4", "Tesla Model S Plaid"])
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


def user_inputs(answer):
    choice = answer
    if choice == "Y" or choice == "y":
        print("Have a safe Trip! (^_^) ")
        cont = False
        invalid = False
    elif choice == "N" or choice == "n":
        print("Let Us please reselect this for you. ")
        cont = True
        invalid = False
    elif choice != "Y" or choice != "y" or choice != "N" or choice != "n":
        print("Invalid choice please try again! ")
        cont = True
        invalid = True

    return invalid





while cont == True:
    invalid = True
    # print("Your destination is", random.choice(destinations))
    print()
    print("Your destination is", trip_destination(destinations))
    while invalid == True:
        choice = input("Would you like this trip? (Y/N) ")
        user_inputs(choice)

















