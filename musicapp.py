from email.mime import text
import os as os
import random as random
import string
print("----------MusicRaq----------")
user_list = ['Tom', 'Bob', 'Bill', 'Alice', 'Mary']

def log_in():
    print("Decrypting User Data...")
    file_path = os.path.join( "Downloads", "airhorn.mp3")
    import random, string
    chars = string.printable
    key = "".join(random.sample(chars, len(chars)))

    

    

    global log_in_name
    print("Log-In selected. Please enter your username")
    
    log_in_name = input("")
    if log_in_name in user_list:
        print("Log In succesfull")
    text = log_in_name
    encrypted = text.translate(str.maketrans(chars, key))
    print(f"Encrypted: {encrypted}")
    print(play_music())
    
def sing_up():
    global sing_up_name
    sign_up_name = input("Enter name to sign up")
    user_list.append(sign_up_name)
    print("Proceed to log in")
    print(log_in())
def play_music():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    airhorn = os.path.join(script_dir, "airhorn.mp3")
    camera = os.path.join(script_dir, "camera.mp3")
    dog = os.path.join(script_dir, "dog.mp3")
    cinematic = os.path.join(script_dir, "cinematic.mp3")
    select_music = input("1, Airhorn 2, Camera 3, Dog 4, Cinematic")
    if select_music == "1":
        os.system(f'mpv --vo=null "{airhorn}"')
        print(play_music())
    elif select_music == "2":
        os.system(f'mpv --vo=null "{camera}"')
        print(play_music())
    elif select_music == "3":
        os.system(f'mpv --vo=null "{dog}"')
        print(play_music())
    elif select_music == "4":
        os.system(f'mpv --vo=null "{cinematic}"')
        print(play_music())
log_option = int(input("Select Option.. 1: Login, 2: Sing-up"))

if log_option == 1:
    print(log_in())
elif log_option == 2:
    print("Sign up")
    print(sing_up())