"""
File Managament Program

Functionalities of the programm
1. Change CWD / Print current CWD
2. Search in CWD
3. Text Editor
"""

import helpers


user_input = helpers.welcome()

match user_input:
    case 1:
        print("\tFunc: Change CWD")
        to_parent = True if input("\tGo back <-: ") == "yes" else False
        
        destination = None
        if not to_parent: destination = input("\tEnter the destination: ")

        try: 
            helpers.change_cwd(to_parent, destination)
        except:
            # make while and add continue
            pass
