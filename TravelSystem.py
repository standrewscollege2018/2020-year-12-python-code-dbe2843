# Travel System task
# Lists for the system
commands = [["Plan Trip: plan"], ["Quit program: quit"]]
departure_locations = [["Christchurch"], ["Wellington"], ["Auckland"]]
overseas_locations = [""]

# Welcoming the user to the Travel System

print ("Hello, this programme allows you to calculate the cost of traveling between places and the cost of accomodation")
print ("Please enter one of the following commands:")
for index in range(0, len(commands)):
    print(commands[index])
run_command = input()
# Running the plan command
if run_command == "plan":
    print ("Select a departure location:")
    for index in range(0, len(departure_locations)):
        print(departure_locations[index])
    run_command = input()    
    departure = input()
    print ("Select a destination:")
    destination = input()