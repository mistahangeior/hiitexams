"""...................................Python  Examination................................................
My Name is Hangeior David Hangeior


"""
import user_crud

#this is the path for the json file
db_path = "db/user.json"

def init():
    # this is a constructor
    print("\n**********WELCOME TO HIIT TECH MINDS**********\n")
    print("Enter 1 to register for participation")
    print("Enter 2 to exit")

    responses = input("Choose an option")

    if responses == "1":
        register()
    elif response == "2":
        print("Thanks for trying to register")
    else:
        print("\nInvalid response \nTry again")
        init()

def register():
    print("\nProvide the following details to create an account")
    name = input("Enter your full name\n")
    email = input("Enter your email\n")
    mobile_no = input("Enter mobile number: \n")

    
    if name == "" or email == ""or mobile_no =="":
        print("\nThese fields cannot be blank")
    else:
        user_details = {
            "name":name,
            "email":email,
            "mobile_no":mobile_no
        }
        response = user_crud.create_user(db_path,user_details)
        if response == 1:
            print("\nUser creation success")
            print("Redirected home")
            init()
        else:
            print("\nUser with such email account already exist")
            prompt("Enter 1 to retry \nEnter anything to go home", init, register)

init()