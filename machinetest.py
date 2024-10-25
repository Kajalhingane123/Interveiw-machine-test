import pandas as pd

while True:
    choice = input("\n1: Add User\n2: Display Users\n3: Exit\nEnter choice: ")
    if choice == '1':
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        phone = input("Enter phone number: ")
        df = pd.DataFrame([[name, email, phone]], columns=["Name", "Email", "Phone"])
        df.to_excel("users.xlsx", index=False, header=False)
        print("User added!\n")
    elif choice == '2':
        try:
            users_df = pd.read_excel("users.xlsx", header=None, names=["Name", "Email", "Phone"])
            print("\nUsers:")
            print(users_df)
        except FileNotFoundError:
            print("No users found.")
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
