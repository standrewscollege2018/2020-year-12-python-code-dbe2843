# Book store program

# Creating a list to store the items
books = [["Lolita", "Vladimir Nabokov", 20], ["Hamlet", "William Shakespeare", 30], ["Crime and Punishment", "Fyodor Dostoyevsky", 40]]
commands = [["Add a book: add"], ["Edit a book: edit"], ["Delete a book: delete"]]

#Welcoming the user and asking for their input
print("Welcome to the bookstore! Please type one of the following commands below.")
for index in range(0, len(commands)):
    print(commands[index])
run_command = input()
'''Running the add command'''
if run_command == "add":
    name = input("Enter book name")
    author = input("Enter an author")
    price = int(input("Enter a price"))
    books.append([name, author, price])
print(books)
'''Running the edit command'''
    
    