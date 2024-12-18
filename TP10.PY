users = []
books = []

def add_user():
    name = input("Enter User Name: ")
    membership_id = len(users) + 1 
    users.append({"id": membership_id, "name": name, "borrowed": 0, "returned": 0})
    print(f"User '{name}' added with Membership ID: {membership_id}")

def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    book_id = len(books) + 1  
    books.append({"id": book_id, "title": title, "author": author, "available": True})
    print(f"Book '{title}' added with Book ID: {book_id}")

def view_users():
    if users:
        print("\nUsers in Library:")
        for user in users:
            print(f"ID: {user['id']}, Name: {user['name']}, Borrowed: {user['borrowed']}, Returned: {user['returned']}")
    else:
        print("No users available.")


def view_books():
    if books:
        print("\nBooks in Library:")
        for book in books:
            status = "Available" if book['available'] else "Issued"
            print(f"ID: {book['id']}, Title: '{book['title']}' by {book['author']} ({status})")
    else:
        print("No books available.")


def issue_book():
    user_id = int(input("Enter User ID: "))
    book_id = int(input("Enter Book ID to issue: "))
    
    user = next((u for u in users if u['id'] == user_id), None)
    book = next((b for b in books if b['id'] == book_id), None)
    
    if user and book:
        if book['available']:
            book['available'] = False
            user['borrowed'] += 1
            print(f"Book '{book['title']}' issued to {user['name']}.")
        else:
            print("Book is already issued.")
    else:
        print("Invalid User ID or Book ID.")


def return_book():
    user_id = int(input("Enter User ID: "))
    book_id = int(input("Enter Book ID to return: "))
    
    user = next((u for u in users if u['id'] == user_id), None)
    book = next((b for b in books if b['id'] == book_id), None)
    
    if user and book:
        if not book['available']:
            book['available'] = True
            user['returned'] += 1
            print(f"Book '{book['title']}' returned by {user['name']}.")
        else:
            print("Book is not issued.")
    else:
        print("Invalid User ID or Book ID.")

def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add User")
        print("2. Add Book")
        print("3. View Users")
        print("4. View Books")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            add_user()
        elif choice == '2':
            add_book()
        elif choice == '3':
            view_users()
        elif choice == '4':
            view_books()
        elif choice == '5':
            issue_book()
        elif choice == '6':
            return_book()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()