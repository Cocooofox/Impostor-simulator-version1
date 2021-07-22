import os

print("WELCOME TO IMPOSTOR SIMULATOR VER1, TYPE start TO START.")
choix = input("\n\nstart? : ")
if choix == 'start':
    print("\n\nYOU NEED TO KILL SOMEONE NOW, YOU HAVE DIFFERENT CHOICES, LIKE :\nRED : Red is just in fornt of medbay, he is a bad player, so you can easily kill him.\nBLUE : Blue is at cams, he also is a bad player, so he is a easy kill too.\nGREEN : Green is a good player, he is in electricity, wich means that you possibly can kill him.\nPINK : Pink is a pro player, he is in nav, we don't know if it is safe to kill him...\nCHOOSE SOMEONE!!")
    imposterfirstkill = input("\n\nCHOOSE WHO TO KILL : ")
    if imposterfirstkill == 'RED':
        print("GAME OVER, THERE IS A CAM AT THE ENTRACE OF MEDBAY, AND BLUE IS AT CAM!!!")
    elif imposterfirstkill == 'BLUE':
        print("GG, YOU'VE JUST MADE YOU'RE FIRST KILL!\n\nYOU NOW HAVE DIFFERENT CHOICES...\nRED : Red is idling in the cafeteria.\nPINK : Pink is doing scan.\nGREEN : Green is watching pink.")
        blueroute = input("\n\nCHOOSE WHO TO KILL : ")
        if blueroute == 'GREEN':
            print("PINK : ARE YA FUCKIN DUMB YO???? HEYA RETURN TO DRAWING, DON'T PLAY THIS GAME DUMBASS")
            os.system("MSPAINT") #this opens you ms paint cuz you're a dumb kid.
        elif blueroute == 'PINK':
            print("GREEN : WHAT THE FUCK BRO?")
        elif blueroute == 'RED':
            print("GG, YOU HAVE JUST MADE YOUR SECOND KILL!\nONE MORE KILL, AND THEN YOU'LL WIN!!\nPINK : Pink is in electrical, and he is doing tasks, but remember, he is a pro player, so we don't know if it is safe to kill him.\nGREEN : Green is eating pitzah™️.")
            blueroutefinal = input("\n\nCHOOSE WHO TO KILL : ")
            if blueroutefinal == 'PINK':
                print("GGGGGGGG, YOU WONNNNN!!!\n You : Well, i guess he wasn't a pro at all lol.")
            elif blueroutefinal == 'GREEN':
                print("GAME OVER, HE JUST FINISHED HIS pitzah™️, AND HE TURNED HIS HEAD WHILE YOU HAD THE KNIFE IN THE HAND.")
    if imposterfirstkill == 'PINK':
        print("GG, YOU'VE JUST MADE YOU'RE FIRST KILL!!\nOH NO!!! RED JUST CAME INTO THE ROOM, WELL, I GUESS IT'S A GAME OVER...")
    if imposterfirstkill == 'GREEN':
        print("GREEN DODGED YOU!!! HE RAN TO REPORT, YOUR DEAD... GAME OVER.") #i hate my job, wait, it's not my job, i'm only a french 13 years old coder, i don't have any job!
if choix == 'sussy boi':
    print("sussy boi is just for testing." + choix)