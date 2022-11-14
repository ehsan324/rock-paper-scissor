from random import randrange
from os import system, name
from colorama import Fore
from pyfiglet import figlet_format
from time import sleep


def display() -> None:
    system("cls" if name == "nt" else "clear")
    print(Fore.GREEN + figlet_format('wellcome gamers', font = 'standard'))
    print('1:rock\n2:paper\n3:scissor')
    
    
def random():
    return randrange(3)
    

def player():
    try:
        return int(input('please enter your choice: '))
    except Exception as e:
        print(e)
        sleep(5)
        player()


def valid(inputs):
    if inputs < 4 and inputs > 0:
        return True
    else:
        print('Error!!\nplease enter correct number between 1 to 3')
        player()
        
        
def compare(bot, player, scores):
    valid(player)
    scoreBot = scores[0]
    scorePlayer = scores[1]
    
    if bot == 1 and player == 3:
        scoreBot += 1
        print(Fore.RED + "bot" + Fore.GREEN + " get score")
    elif bot == 2 and player == 1:
        scoreBot += 1
        print(Fore.RED + "bot" + Fore.GREEN + " get score")
    elif bot == 3 and player == 2:
        scoreBot += 1
        print(Fore.RED + "bot" + Fore.GREEN + " get score")
    elif bot == 3 and player ==1:
        scorePlayer += 1
        print(Fore.RED + "player" + Fore.GREEN + " get score")
    elif bot == 1 and player == 2:
        scorePlayer += 1
        print(Fore.RED + "player" + Fore.GREEN + " get score")
    elif bot == 2 and player == 3:
        scorePlayer += 1
        print(Fore.RED + "player" + Fore.GREEN + " get score")
    else:
        print(Fore.RED + "draw")
    
    scores[0] = scoreBot
    scores[1] = scorePlayer
    
    return scores

    
def main():
    status = True
    scores = [0, 0]
    while status:
        display()
        scores = compare(random(), player(), scores)
        
        print(Fore.CYAN + "bot score: " + Fore.RED + str(scores[0]) + Fore.CYAN + "\nplayer score: " + Fore.RED + str(scores[1]) + Fore.RESET)
        
        if 'N' == input("do you want continue? (N-> exit) ").upper():
            print('Goodbye')
            exit(0)
        
        
if __name__ == "__main__":
    main()
    