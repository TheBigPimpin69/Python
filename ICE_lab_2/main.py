# Lab 2
# 1207-01
# 2024-02-08
# Max Noyes, Brady Cousins, Eamonn Patterson, Rajveer Mashruwala, Riddhi Tandel

# Link for the test case: https://docs.google.com/spreadsheets/d/1FCsPrXfAPY4LwGmUCvKaViewF-TIxQAYNG43nWn7u9A/edit?usp=sharing

# This program allows the user to use three features: add a book to a csv file,
# retrieve all books from the file, or search for a specific book as well as
# exit the program.

# importing needed modules
import csv
import os

# Check if the 'books.csv' file exists, if not, create it
if not os.path.exists("books.csv"):
    with open("books.csv", "w", newline="") as file:
        pass


# Function to add a book to the CSV file
def add_book():
    title = input("Enter the title of the book: ")
    author_name = input("Enter the author's name: ")
    year_publication = input("Enter the year of publication: ")

    # adding the input to a list and writing to the file
    try:
        int(year_publication)
        booklist = [title, author_name, year_publication]
        with open("books.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(booklist)
        print('Book added successfully.')
    except ValueError:
        print('Invalid year of publication. Please enter an integer.')


# Function to retrieve all books from the CSV file
def retrieve_books():
    try:
        with open('books.csv', 'r') as file:
            reader = csv.reader(file)
            for i, book in enumerate(reader, start=1):
                print(f"{i}. Title: {book[0]}, Author: {book[1]}, Year: {book[2]}")
    except FileNotFoundError:
        print("No books found in the reading list.")


# Function to search for a book by title in the CSV file
def search_book(title):
    try:
        with open('books.csv', 'r') as file:
            reader = csv.reader(file)
            found = False
            for book in reader:
                if book[0].lower() == title.lower():
                    print("Results:")
                    print(f"Title: {book[0]}, Author: {book[1]}, Year: {book[2]}")
                    found = True
                    break
            if not found:
                print("Error: Book not found.")
    except FileNotFoundError:
        print("No books found in the reading list.")


# Main loop to display the menu and handle user choices
while True:
    try:
        print("\nPlease select which option you would like: ")
        print("1. Add a book")
        print("2. Search for a book")
        print("3. Retrieve all books")
        print("4. Exit")

        # getting the choice for the option they want to use
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book()
        elif choice == 2:
            title = input("Enter the title of the book to search: ")
            search_book(title)
        elif choice == 3:
            retrieve_books()
        elif choice == 4:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter a number.")
