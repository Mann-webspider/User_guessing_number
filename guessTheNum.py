import random 
def compNum():
    rand=random.randint(1,500)
    return rand 

def userGuess(num):
    global comp
    if(num < comp):
        print("your number is too low")
    elif(num>comp):
        print("your number is too high")
    else:
        print(f"you get the correct number{comp},{num}")
        return False

def playAgain():
    end = input("--------------if you want to play again press Enter or if you want to exit TYPE exit : ------------------\n")
    end = end.lower()
    if end == "":
        play()
    elif end == "exit":
        exit()
    else:
        print("INVALID INPUT READ INSTRUCTION CAREFULLY")
        playAgain()

def play():
    comp=compNum() 
    
    while True:
        num = int(input("enter your guess number: "))
        # userGuess(num)
        if(num < comp):
            print("your number is too low")
        elif(num>comp):
            print("your number is too high")
        else:
            print(f"you get the correct number{comp},{num}")
            break
    playAgain()
    
play()