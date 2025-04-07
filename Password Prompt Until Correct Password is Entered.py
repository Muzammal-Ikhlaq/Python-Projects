correct_password = "Python123"  # Set the correct password

while True:
    password = input("Enter the password: ")  # Ask user for password
    if password == correct_password:
        print("Access Granted!")
        break  # Exit loop if password is correct
    else:
        print("Incorrect password. Try again.")