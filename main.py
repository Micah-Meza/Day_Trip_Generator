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

# These def allows for randome choices.









def run_day_trip_plan():
    destinations = ["Canada", "Spain", "Tokyo", "London", "Fiji Island"]
    restaurants = ["Noma", "Geranium", "Asador Etxebarri", "Disfrutar Frantzén", "McDonalds"]
    transportation_selections = ["Rolls-Royce Phantom", "Bugatti Chiron", "Private Jet", "Public Plane", "Helicopter"]
    entertainment_selections = ["Skydiving", "Concert", "Mountain Climbing", "Space Walk", "Escape Island"]
    des = generate_random_plan(destinations)
    res = generate_random_plan(restaurants)
    tra = generate_random_plan(transportation_selections)
    ent = generate_random_plan(entertainment_selections)
    trip_plan = [des, res, tra, ent]
    print_full_trip(trip_plan)


    
    selected_choice = reselect_trip(choice)







    print()


def print_full_trip(trip_option):
    print("Destination: {}\nRestaurant {}\nTransportation {}\nEntertainment {}\n.".format(trip_option))
    choice = input("Are you happy with the selections? (Y/N) ")
    
    return choice


def generate_random_plan(item_lists):
    item_lists = random.choice(item_lists)
    return item_lists


def choice_option(current_trip, trip_option):
    invalid = True
    while invalid == True:
        choice = input("Would like to keep entertainment selection? (Y/N) ")
        if choice == "Y" or choice == "y":
            print("Confirmed")
            print()
            answer = False
            invalid = False
        elif choice == "N" or choice == "n":

            print("Let Us please reselect this for you. ")
            answer = True
            invalid = False
        elif choice != "Y" or choice != "y" or choice != "N" or choice != "n":
            print("Invalid choice please try again! ")

            invalid = True
    return answer


def reselect_trip(current_trip, options):
    









    print()


run_day_trip_plan()









# def trip_destination(places):
#     places = random.choice(places)
#     return places

# def trip_restaurants(foods):
#     foods = random.choice(foods)
#     return foods

# def trip_tranportation(cars):
#     cars = random.choice(cars)
#     return cars

# def trip_entertainment(activities):
#     activities = random.choice(activities)
#     return activities

# These def process the user input and validates the correct choice.
# def destination_choice(answer):
#     invalid = True
#     while invalid == True:
#         choice = input("Would you like to keep this destination selection? (Y/N) ")
#         if choice == "Y" or choice == "y":
#             print("Confirmed")
#             print()
#             answer = False
#             invalid = False
#         elif choice == "N" or choice == "n":
#             print("Let Us please reselect this for you. ")
#             answer = True
#             invalid = False
#         elif choice != "Y" or choice != "y" or choice != "N" or choice != "n":
#             print("Invalid choice please try again! ")
#             invalid = True
#     return answer


# def transportation_choice(answer):
#     invalid = True
#     while invalid == True:
#         choice = input("Do you wish to keep this transportation selection? (Y/N) ")
#         if choice == "Y" or choice == "y":
#             print("Confirmed")
#             print()
#             answer = False
#             invalid = False
#         elif choice == "N" or choice == "n":
#             print("Let Us please reselect this for you. ")
#             answer = True
#             invalid = False
#         elif choice != "Y" or choice != "y" or choice != "N" or choice != "n":
#             print("Invalid choice please try again! ")
#             print()
#             invalid = True
#     return answer


# def restaurants_choice(answer):
#     invalid = True
#     while invalid == True:
#         choice = input("Would you like to keep this restaurant choice? (Y/N) ")
#         if choice == "Y" or choice == "y":
#             print("Confirmed")
#             print()
#             answer = False
#             invalid = False
#         elif choice == "N" or choice == "n":
#             print("Let Us please reselect this for you. ")
#             answer = True
#             invalid = False
#         elif choice != "Y" or choice != "y" or choice != "N" or choice != "n":
#             print("Invalid choice please try again! ")
#             invalid = True
#     return answer


# def entertainment_choice(answer):
#     invalid = True
#     while invalid == True:
#         choice = input("Would like to keep entertainment selection? (Y/N) ")
#         if choice == "Y" or choice == "y":
#             print("Confirmed")
#             print()
#             answer = False
#             invalid = False
#         elif choice == "N" or choice == "n":

#             print("Let Us please reselect this for you. ")
#             answer = True
#             invalid = False
#         elif choice != "Y" or choice != "y" or choice != "N" or choice != "n":
#             print("Invalid choice please try again! ")

#             invalid = True
#     return answer

# destinations = ["Canada", "Spain", "Tokyo", "London", "Fiji Island"]
# restaurants = ["Noma", "Geranium", "Asador Etxebarri", "Disfrutar Frantzén", "McDonalds"]
# transportation_selections = ["Rolls-Royce Phantom", "Bugatti Chiron", "Private Jet", "Public Plane", "Helicopter"]
# entertainment_selections = ["Skydiving", "Concert", "Mountain Climbing", "Space Walk", "Escape Island"]



# def run_day_trip_plan():


# The main program.
# cont = True
# while cont == True:
#     print()
#     trip_location = trip_destination(destinations)
#     print("The destination choosen is {}!".format(trip_location))
#     cont = destination_choice(cont)
#     if cont == True:
#         destinations.remove(trip_location)
#     elif cont == False:
#         print("********************************************************")
        
# cont_1 = True
# while cont_1 == True:
#     print()
#     trip_ride = trip_tranportation(transportation_selections)
#     print("Your transportation would be a {}!".format(trip_ride))
#     cont_1 = transportation_choice(cont_1)
#     if cont_1 == True:
#         transportation_selections.remove(trip_ride)
#     elif cont_1 == False:
#         print("********************************************************")

# cont_2 = True
# while cont_2  == True:
#     print()
#     trip_food = trip_restaurants(restaurants)
#     print("You will dine at {}!".format(trip_food))
#     cont_2  = restaurants_choice(cont_2)
#     if cont_2  == True:
#         restaurants.remove(trip_food)
#     elif cont_2  == False:
#         print("********************************************************")

# cont_3 = True
# while cont_3 == True:
#     print()
#     trip_fun = trip_entertainment(entertainment_selections)
#     print("The activity choosen is a {}!".format(trip_fun))
#     cont_3 = entertainment_choice(cont_3 )
#     if cont_3 == True:
#         entertainment_selections.remove(trip_fun)
#     elif cont_3 == False:
#         print("********************************************************")

# print()
# print("Your entertainment will be a {} and you will travel to {} while being transported by a(n) {} and dining at {}.".format(trip_fun, trip_location, trip_ride, trip_food))
# print() 
