import random

finish_words = ["goodbye", "close", "exit"]

all_users = {}

def input_error(func):

    """
    This function decorates the handler functions and works with exceptions

    """


    def inner(user_command):

        try:

            res_func = func(user_command)

        except KeyError:

            print("Please, enter the command and the user's name from dict")

        except IndexError:

            print("Please, enter the command and user's data")

        except ValueError:

            print("Please, enter the command and user's name and the phone")

        else:

            return res_func

    return inner

@input_error
def add_user(user_command):
    
    """
    This function takes the user's name and phone and add to the dictionary.
    If the user's name is already in dict, the random number will be added
    to the user's name and the user will get the message with new name
    for using in future

    """
    user_data = user_command.split(" ")

    phone = int(user_data[2])
    
    if not user_data[1] in all_users:
        
        all_users[user_data[1]] = user_data[2]

    else:

        user_data[1] = user_data[1] + str(random.randint(1, 1000))
        all_users[user_data[1]] = user_data[2]
        return f"written as {user_data[1]} because your name was in the dictionary"

@input_error
def change_phone(user_command):

    """

    This function takes the user's name and phone and change the phone number
    in the dictionary according to the user's name.
    If the user's name is not in dict, the user will get the message about it.
    
    """
    

    user_data = user_command.split(" ")
    phone = int(user_data[2])

    if user_data[1] in all_users:

        all_users[user_data[1]] = user_data[2]

    else:

        return f"{user_data[1]} is not in the users dictionary"
    
@input_error
def show_phone(user_command):
    
    """
    This function shows the phone number if the user is in dictionary.
    If not - the user will get the message about it
    """
    
    user_data = user_command.split(" ")

    if user_data[1] in all_users:
        return all_users[user_data[1]]
    else:
        return f"{user_data[1]} is not in the users dictionary"

@input_error
def show_all_users(user_command):

    """
    This function shows the users and their phone numbers 
    
    """
    
    return all_users

    
    
COMMAND_WORDS = {
    "add": add_user,
    "change": change_phone,
    "phone": show_phone,
    "show all": show_all_users
    }

def get_handler(command_word):
    
    
    return COMMAND_WORDS[command_word]


def main():

    """
    This function takes the command from user and do what the user asks.
    It stops the process when the key words are entered

    """

    while True:

        user_command = input()
        user_command_small_letters = user_command.lower()

        if user_command_small_letters == "hello":
            print("How can I help you?")

        for word in COMMAND_WORDS:

            if user_command_small_letters.startswith(word):
                
                handler = get_handler(word)
               
                func_result = handler(user_command)

                if func_result:
                    print(func_result)


        if user_command_small_letters in finish_words:
            break
        
    print("Good bye!")


if __name__ == '__main__':
    main()
