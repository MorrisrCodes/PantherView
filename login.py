import sqlite3

# Create or connect to the database
conn = sqlite3.connect('login_db.db')
cursor = conn.cursor()

# Create the users table if it doesn't already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    email TEXT UNIQUE,
                    displayname TEXT UNIQUE,
                    password TEXT
                )''')
conn.commit()

def signup():
    print("Signup")
    email = input("Enter your email: ")
    
    # Check if the email already exists
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    if cursor.fetchone():
        print("Email already exists. Please login or use a different email.")
        return
    
    password = input("Enter your password: ")
    
    # Get and validate display name
    while True:
        displayname = input("Choose a display name: ")
        
        # Check if display name already exists
        cursor.execute("SELECT * FROM users WHERE displayname = ?", (displayname,))
        if cursor.fetchone():
            print("Display name already taken. Please choose another one.")
        else:
            break
    
    # Insert the new user into the database
    cursor.execute("INSERT INTO users (email, displayname, password) VALUES (?, ?, ?)", 
                   (email, displayname, password))
    conn.commit()
    print(f"Account created successfully! Welcome {displayname}.")

def login():
    print("Login")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    # Fetch user data based on email
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    
    if user:
        stored_password = user[2]  # The plain password stored in DB
        if password == stored_password:
            print(f"Login successful! Welcome {user[1]}.")  # Display name is at index 1
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Email not found. Please sign up first.")

def main():
    print("Welcome to Pantherview!")
    while True:
        choice = input("Would you like to login or signup? (Enter 'login' or 'signup'): ").lower()
        if choice == 'signup':
            signup()
            break  # Exit after signup
        elif choice == 'login':
            login()
            break  # Exit after login
        else:
            print("Invalid choice. Please enter 'login' or 'signup'.")

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
