#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                             Import packages and python modules
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from Spy_details import spy

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                            Function to add a status or update a status
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_status_message(current_status):
    STATUS_MESSAGE = []
    if current_status!=None :
        print("Your current status is"+current_status+"\n")
    else:
        print("You don't have any status message currently \n")
    default_value = raw_input("Would you like to set from your older statuses? (Y/N)")
    if default_value.upper()=='N':
        new_status_message = raw_input("What status message do you want to set")
        if len(new_status_message)>0:
            updated_status_message = new_status_message
            STATUS_MESSAGE.append(updated_status_message)
            print(STATUS_MESSAGE)
    elif default_value.upper()=='Y':
        item_position = 1
        for message in STATUS_MESSAGE:
            print(item_position+". "+message)
            item_position = item_position+1
        message_selection = int(raw_input("Choose from the above messages:"))
        if len(STATUS_MESSAGE)>= message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection-1]
    return updated_status_message

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                    Function to add a friend
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

friends = {}
def add_friend():
    new_friend = {
    'name': '',
    'salutation': '',
    'age': 0,
    'rating': 0.0,
    'chats': []
    }
    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
    new_friend['age'] = raw_input("Age?")
    new_friend['rating'] = raw_input("Spy rating?")
    if len ( new_friend['name'] ) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append ( new_friend )
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len ( friends )


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                   Function to initiate a chat
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def start_chat(spy_name, spy_age, spy_rating): #currently not using the parameters
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_option = int ( raw_input ("What would you like to do \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read chats from a user \n 6. Close the application" ) )
        if menu_option==1:
            current_status_message = add_status_message(current_status_message)
            print("Added a new status")
            break
        elif menu_option==2:
            print("Added a friend")
            break
        elif menu_option==3:
            print("Send a secret message initiated......")
            break
        elif menu_option==4:
            print("Read a secret message initiated......")
            break
        elif menu_option==5:
            print("Reading chat from user")
            break
        elif menu_option==6:
            print("Exiting now.....")
            show_menu = False
        else:
            print("Invalid Option select from 1 to 6")


spy_is_online = False #status of the spy
user_option = raw_input("Would you like to continue as a default user (default) or create your own (new)? ") #type of user

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def select_friend():
     item_number = 0
     for friend in friends:
         print()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                       Code for continuing as a new user 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if user_option == "new":
    spy_name = raw_input("Welcome to SpyChat, you must tell me you Spyname first:" )
    if len ( spy_name ) > 0: #to calculate the length of the string
        print('Welcome ' + spy_name + ' Glad to have you with us.')
        spy_salutation = raw_input ( "What should I call you Mr. or Ms. ?" )
        print('Alright ' + spy_salutation + '.' + spy_name + ' I\'d like to know a little bit more about you before we proceed')
    else:
        print('A spy needs to have a valid name. Please try again.')
    spy_age = int(input('What is your age? ')) #age of the spy
    if spy_age>12 and spy_age<50:
        spy_rating = float(raw_input('What is your spy rating? '))
        if spy_rating>4.5:
            print('Great Ace!')
        elif spy_rating>3.5 and spy_rating<=4.5:
            print('You are one of the good ones.')
        elif spy_rating>=2.5 and spy_rating<=3.5:
            print('You can always do better')
        else:
            print('We can always use somebody to help in the office. ')
    else:
    print('Sorry you are not of the correct age to become a spy.') #entered age is not between 12 and 50
    print('Authentication Complete. We are glad to have you with us. Welcome '+spy_salutation+'.'+spy_name+", Your sp rating is "+str(spy_rating)) #float value to string value
    spy_is_online = True
    print('Changing the status of spy from offline to online '+str(spy_is_online)) #bool value to string value for concatenation
    start_chat(spy_name,spy_age,spy_rating) # calling menu option

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                           Code for continuing as a default user
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

elif user_option=='default':
    print('Authentication Complete. We are glad to have you with us. Welcome ' + Default_user().spy_salutation + '.' + Default_user().spy_name + ", Your sp rating is " + str(Default_user().spy_rating))  # float value to string value
    spy_is_online = True
    start_chat(spy['name'],spy['age'],spy['rating']) # calling menu option
else:
    print("Please select default user or create a new one.")










