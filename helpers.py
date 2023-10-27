"""
Functions used in the program

"""

import pathlib

def welcome():
    user_input = int(input("What to do: "))
    while user_input not in range(1,4):
        print(user_input)
        if user_input in range(1,4):
            break
        welcome()
        
    return user_input

def change_cwd(destination: pathlib.Path):
    try:
        cwd = pathlib.Path.cwd()
        cwd = cwd / f"{destination}"
        print(f"\tNow you are in: {cwd}")   
    except:
        print("Try later.")

if __name__ == "__main__":
    print("You run the module! Not the main application") 
    print("Please run the main.py")