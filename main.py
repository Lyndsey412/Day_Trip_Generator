destination_option = ['Pittsburgh, PA', 'Washington, D.C.', 'New Orleans']
restaraunt_styles = ['Italian', 'French', 'American']
mode_of_transportation = ['Uber', 'Rental Car', 'Scooter']
types_of_entertainment = ['Concert', 'Museum', 'The Zoo']

def generate_trip():
    user_input = ''
    while user_input != 'y':
        introduction = "Hello, we have selected the following itinerary for you to explore."
        print(introduction)

import random 
destination_option = ['Pittsburgh, PA', 'Washington, D.C.', 'New Orleans']
choose_destination = random.choice(destination_option)
print(choose_destination)

restaraunt_styles = ['Italian', 'French', 'American']
choice_of_restaraunt = random.choice(restaraunt_styles)
print(choice_of_restaraunt)

mode_of_transportation = ['Uber', 'Rental Car', 'Scooter']
choice_of_transportation = random.choice(mode_of_transportation)
print(choice_of_transportation)

types_of_entertainment = ['Concert', 'Museum', 'The Zoo']
choice_of_entertainment = random.choice(types_of_entertainment)
print(choice_of_entertainment)

user_input = input("Would you like to confirm this trip? 'y' to confirm/'n' to modify:")

def user_confirmation(choice_of_entertainment, choice_of_transportation, choice_of_restaraunt, choose_destination):
    user_confirmation = False
    while user_confirmation is False:
        random.choice = user_confirmation()
        user_confirmation = input(f"We have selected {choose_destination}, as your {destination_option}. Are you satisfied with this? y/n: ")
        if user_confirmation == "y":
            user_confirmation = True
    return random.choice

# def get_random_selection(list_of_options):
#     return random.choice(list_of_options)



