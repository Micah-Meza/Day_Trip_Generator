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
restaurants = ["Noma", "Geranium", "Asador Etxebarri", "Disfrutar Frantzén", "McDonalds"]
transportation_selections = ["Rolls-Royce Phantom", "Bugatti Chiron", "Private Jet", "Public Plane", "Helicopter"]
entertainment_selections = ["Skydiving", "Concert", "Mountain Climbing", "Space Walk", "Escape Island"]

def run_day_trip_plan():
    destination = generate_random_plan(destinations)
    restaurant = generate_random_plan(restaurants)
    transportation = generate_random_plan(transportation_selections)
    entertainment = generate_random_plan(entertainment_selections)
    trip_plan = [des, res, tra, ent]
    print_full_trip(trip_plan)
    print()
    trip_confirmation(destination, restaurant, transportation, entertainment)
    

def trip_confirmation(destination, restaurant, transportation, entertainment):
        trip_plan = [destination, restaurant, transportation, entertainment]
        cont = True
        while cont == True:
            select = input("Are you satisfied with the selections? (Y/N) ")
            if select == "n":
                trip_option = input("Which would you like to change: Destination, Resataurant, Transportation, or Entertainment? ")
                print()
                reselect_trip(trip_option, trip_plan)
                cont = True              
            elif select == "y":
                print()
                print("Here's is your final list: ")
                print_full_trip(trip_plan)
                print()
                cont = False
                

def print_full_trip(trip_option):
    print("Destination: {}\nRestaurant: {}\nTransportation: {}\nEntertainment: {}".format(trip_option[0],trip_option[1],trip_option[2],trip_option[3]))


def generate_random_plan(item_lists):
    item_lists = random.choice(item_lists)
    return item_lists


def reselect_trip(trip_option, new):
        if trip_option == "Destination" or trip_option == "destination":
            new = new
            destination = generate_random_plan(destinations)
            new.pop(0)
            new.insert(0, destination)
            print_full_trip(new)
            print()

        elif trip_option == "Restaurant" or trip_option == "restaurant":
            new = new
            restaurant = generate_random_plan(restaurants)
            new.pop(1)
            new.insert(1, restaurant)
            print_full_trip(new)
            print()

        elif trip_option == "Transportation" or trip_option == "transportation":
            new = new
            transportation = generate_random_plan(transportation_selections)
            new.pop(2)
            new.insert(2, transportation)
            print_full_trip(new)
            print()

        elif trip_option == "Entertainment" or trip_option == "entertainment":
            new = new
            entertainment = generate_random_plan(entertainment_selections)
            new.pop(3)
            new.insert(3, entertainment)
            print_full_trip(new)
            print()

        else:
            print("Invalid choice please try again! ")


run_day_trip_plan()



