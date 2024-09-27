def register():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Enter your confirm password: ")

    if name == "" or email == "" or password == "" or confirm_password == "":
        print("All fields are required.")
    elif password != confirm_password:
        print("Passwords do not match.")
    else:
        with open("registration.txt", "a") as file:
            file.write(f"Name: {name}\nEmail: {email}\nPassword: {password}\n\n")
            print("Registration successful.")

def main():
    print("REGISTRATION FORM")
    print("------------------")
    register()

if __name__ == "__main__":
    main()
