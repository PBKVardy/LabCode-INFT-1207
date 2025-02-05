import csv


# Function to add a book to the reading list
def add_book(title, author, year):
    # Add validation to make sure you input all data
    if title is None or title.strip() == "":
        return "Error: Title cannot be empty."
    if author is None or author.strip() == "":
        return "Error: Author cannot be empty."
    if year is None or year.strip() == "":
        return "Error: Year cannot be empty."
    if not year.isnumeric() and not year.lower().endswith('bc') and not year.lower().endswith('ad') and not year.lower().endswith('bce') and not year.lower().endswith('ce'):
        return "Error: Year must be a number."

    with open('books.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])

# Function to list all books
def list_books():
    with open('books.csv', mode='r') as file:
        to_print = ""
        reader = csv.reader(file)
        for row in reader:
            to_print += f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}\n'
        return to_print.rstrip()


# Function to search for a book by title
def search_book(title):
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == title.lower():
                return f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}'

        return 'Book not found'


# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            output = add_book(title, author, year)
            if output: print(output)
        elif choice == '2':
            print(list_books())
        elif choice == '3':
            title = input("Enter book title to search: ")
            print(search_book(title))
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    menu()
