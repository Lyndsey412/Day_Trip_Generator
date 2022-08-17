destination_option = ['Pittsburgh, PA', 'Washington, D.C.', 'New Orleans']
restaraunt_styles = ['Italian', 'French', 'American']
mode_of_transportation = ['Uber', 'Rental Car', 'Scooter']
types_of_entertainment = ['Concert', 'Museum', 'The Zoo']


introduction = "Hello, we have selected the following itinerary for you to explore."
print(introduction)

def total_trip_generator(list1):
    import random
    total_trip_generator = random.choice(list1)
    print(total_trip_generator)

total_trip_generator(destination_option)
total_trip_generator(restaraunt_styles)
total_trip_generator(mode_of_transportation)