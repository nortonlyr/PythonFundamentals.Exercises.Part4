from random import randrange

def guess(): 
    """
    Enter guess number
    """
    global yourNum
    yourNum = int(input('Give me a number between 0 and 10: '))
    print('Your guess was: ' + str(yourNum))
 

def generateRandomNum():
    """
    Generate a random number
    """
    global randomNum
    randomNum = randrange(0,10)

generateRandomNum()



def checkYourNumber():
    """
    Compare the guess number and radomn number
    """
    while True:
        guess()
        if yourNum > randomNum:
            print('Too high')
        elif yourNum < randomNum:
            print('Too low')
        else:
            print('Congratulation')
            break

checkYourNumber()