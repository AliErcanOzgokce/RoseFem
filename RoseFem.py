import functions
import os
from sty import fg
print(fg(255, 10, 10) + """
 ██▀███   ▒█████    ██████ ▓█████   █████▒▓█████  ███▄ ▄███▓
▓██ ▒ ██▒▒██▒  ██▒▒██    ▒ ▓█   ▀ ▓██   ▒ ▓█   ▀ ▓██▒▀█▀ ██▒
▓██ ░▄█ ▒▒██░  ██▒░ ▓██▄   ▒███   ▒████ ░ ▒███   ▓██    ▓██░
▒██▀▀█▄  ▒██   ██░  ▒   ██▒▒▓█  ▄ ░▓█▒  ░ ▒▓█  ▄ ▒██    ▒██ 
░██▓ ▒██▒░ ████▓▒░▒██████▒▒░▒████▒░▒█░    ░▒████▒▒██▒   ░██▒
░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒ ░    ░░ ▒░ ░░ ▒░   ░  ░
  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░ ░       ░ ░  ░░  ░      ░
  ░░   ░ ░ ░ ░ ▒  ░  ░  ░     ░    ░ ░       ░   ░      ░   
   ░         ░ ░        ░     ░  ░           ░  ░       ░   
                                         by @AliErcanOzgokce
""" + fg.rs)
print(fg(247,242,231)+ """


Passwor Generator MODES:

[1] Full Mode                          (All Symbols,Digits,Letters)
[2] Only Upper Letters                 (max Length = 25)
[3] Only Lower Letters                 (max Length = 25)
[4] Only Symbols                       (max Length = 29)
[5] Only Digits                        (max Length = 10)
[6] Upper and Lower Letters            (max Length = 50)
[7] Upper Letters and Digits           (max Length = 35)
[8] Upper Letters and Symbols          (max Length = 54)
[9] Lower Letters and Digits           (max Length = 35)
[10] Lower Letters and Symbols         (max Length = 54)
[11] Upper, Lower Letters and Digits   (max Length = 60)
[12] Lower Letters, Digits and Symbols (max Length = 64)


"""+fg.rs)


while True:
    generator_choice = int(input("Which Mode?:"))
    if generator_choice == 1:
        functions.full()
        choice = input("Would You Like To Create A New Password?(Y/n):")
        if choice in ["Yes","yes","y","Y"]:
            pass
        else:
            break
    if generator_choice == 2:
        functions.only_upper()
        choice = input("Would You Like To Create A New Password?(Y/n):")
        if choice in ["Yes","yes","y","Y"]:
            pass
        else:
            break
    if generator_choice == 3:
        functions.only_lower()
        choice = input("Would You Like To Create A New Password?(Y/n):")
        if choice in ["Yes","yes","y","Y"]:
            pass
        else:
            break
    if generator_choice == 4:
        functions.only_syms()
        choice = input("Would You Like To Create A New Password?(Y/n):")
        if choice in ["Yes","yes","y","Y"]:
            pass
        else:
            break
    if generator_choice == 5:
        functions.only_nums()
        choice = input("Would You Like To Create A New Password?(Y/n):")
        if choice in ["Yes","yes","y","Y"]:
            pass
        else:
            break
    if generator_choice == 6:
        functions.upper_lower()
        choice = input("Would You Like To Create A New Password?(Y/n):")
        if choice in ["Yes","yes","y","Y"]:
            pass
        else:
            break
    if generator_choice == 7:
        functions.upper_nums()
        choice = input("Would You Like To Create A New Password?(Y/n):")
        if choice in ["Yes","yes","y","Y"]:
            pass
        else:
            break
    if generator_choice == 8:
        functions.upper_symbols()
        choice = input("Would You Like To Create A New Password?(Y/n):")
        if choice in ["Yes","yes","y","Y"]:
            pass
        else:
            break
    if generator_choice == 9:
        functions.lower_nums()
        choice = input("Would You Like To Create A New Password?(Y/n):")
        if choice in ["Yes","yes","y","Y"]:
            pass
        else:
            break
    if generator_choice == 10:
        functions.lower_symbols()
        choice = input("Would You Like To Create A New Password?(Y/n):")
        if choice in ["Yes","yes","y","Y"]:
            pass
        else:
            break
    if generator_choice == 11:
        functions.upper_lower_nums()
        choice = input("Would You Like To Create A New Password?(Y/n):")
        if choice in ["Yes","yes","y","Y"]:
            pass
        else:
            break
    if generator_choice == 12:
        functions.lower_nums_symbols()
        choice = input("Would You Like To Create A New Password?(Y/n):")
        if choice in ["Yes","yes","y","Y"]:
            pass
        else:
            break
