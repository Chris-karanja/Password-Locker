#!/usr/bin/env python3.6	 
from user import User 
from credentials import Credentials 


def create_user(username, email, password): 
     ''' Function to create a new user '''	     
     new_user = User(username, email, password)	     
     return new_user 

def create_credential(platform, platform_username, platform_password): 
     ''' Function to create a new credential '''	     
     new_credential = Credential(platform, platform_username, platform_password)	    
     return new_credential 

def save_User(user): 
     ''' Function to save use '''	    
     user.add_user()	     

def save_Credential(credential): 
     ''' Function to save use '''	     
     credential.add_credentials()	     

def find_user(persona, secret): 
     ''' Function that finds a user by persona and returns the user '''	
     return Contact.user(persona, secret) 

def find_credential(network): 
     return Credential.find_credential(network) 

def display_users(): 
     ''' Function that returns all the saved users '''	     
     return Contact.display_users() 

def display_credentials(): 
    ''' Function that returns all the saved users '''	    
    return Credential.display_credentials()

def user_exist():
    ''' Function that returns true or false if user exists '''
    return User.user_exist(network)

def credential_exist():
    ''' Function that returns true or false if credential exists '''
    return Credential.credential_exist(network)

def main():
        print("Hello Welcome to your contact list. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

     while True:
                    print("Use these commands : cu - create a new user, du - display users, ac - add credentials, dc - display credentials, ex -exit the password locker ")


                    command = input().lower()

#if command == 'cu':

            print("New User")
            print("-"*10)

            print ("Username")
            username = input()

            print("Email")
            email = input()

            print("Password")
            password = input()

            save_User(create_user(username, email, password)) # create and save new contact.
            print ('\n')

            print(f"New Contact {username} {email} created")

            print ('\n')

elif command == 'dc':
    if display_credentials():

        print("Here is a list of all your credentials")
        print('\n')

for credential in credential.display_credentials():

    print(f"{credential.platform}")
    print('\n')

else:

    print('\n')
    print("You dont seem to have any credentials saved yet")
    print('\n')

#elif command == "du":

   # display_users()

#elif command == 'ac':

    platform = input()
    print("platform username: ")

    platform_username = input()
    print("Password: ")
    platform_password = input()

    save_Credential(create_credential(platform, platform_username, platform_password)) # create and save new contact.
    print ('\n')
    print(f"New Account {platform} for {platform_username} created")
    print ('\n')

#elif command == "ex":

    print("Bye .......")
#break
    
#else:
    print("INVALID COMMAND! .. Try again")
if __name__ == '__main__':
    main()
