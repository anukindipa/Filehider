import os
import subprocess
import time

origin_path = ''
# change origin path to the path wich you have stored your locker
# use this format "C:\\Users\\You"

password = "enter your password"


def lock():
    """Locks the folder"""
    print('you are locking')
    subprocess.run('ren Locker "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"', shell=True)
    subprocess.run('attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"', shell=True)


def unlock():
    """Unlocks the folder"""
    print("you are unlocking")
    subprocess.run('attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"', shell=True)
    subprocess.run('ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Locker', shell=True)


def md():
    """Makes new directory if it doesn't already exists"""
    os.mkdir("Locker")
    print('New Locker has been made'
    '\n;)')



def if_y():    
    unlock()
    npath = origin_path
    npath = os.path.realpath(npath)
    os.startfile(npath) 
    time.sleep(0.2)

def main():

    print("Welcome")
    os.chdir(origin_path)
    a = os.listdir()
    
    
    if "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" in a:
        Pword = input("enter password\n")

        if Pword == password:
            inputt = input("Do you want to open your directory now")
            if inputt == "y":
                if_y()
            elif inputt == "yes":
                if_y()             
            else:
                unlock()
        else:
            print('wrong password')
            time.sleep(0.2)
            exit()

    elif "Locker" in a:
        lock()
        time.sleep(0.2)

    else:
        md()
        time.sleep(0.2)


# Use this 
# pyinstaller -F -i <icon path> main.py
# ex -> pyinstaller -F -i Dir\file.ico main.py

main()