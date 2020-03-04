# Travel System task
# Lists for the system
departure_locations = [["Christchurch"], ["Wellington"], ["Auckland"]]
overseas_locations = [""]

# Welcoming the user to the Travel System

print ("Hello, this programme allows you to calculate the cost of traveling between places and the cost of accomodation")
print ('''Please enter one of the following commands:
   1) Plan a flight
   2) Quit program''')
run_command = int(input())
# Running the plan command
if run_command == 1:
    # Selecting a departure location
    print ("Select a departure location:")
    for index in range(0, len(departure_locations)):
        print(index+1, departure_locations[index][0])  
    departure = input()
    # Select a destination
    print ("Select a destination:")
    destination = input()