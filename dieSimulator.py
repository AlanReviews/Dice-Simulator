import random

ITERATIONS = 9999999

def roll_die():
    rolls = []
    for i in range(0, 6):
        rolls.append(random.randint(1, 6))
    return rolls

def checkWinner(array):
    array.sort()
    temp = array[0]
    count = 1
    for i in range(1, 6):
        if (temp == array[i]):
            count+=1
            if (count == 3):
                return True
        else:
            temp = array[i]
            count = 1
    return False

def main():
    winners = 0
    for i in range(0, ITERATIONS):
        rolls = roll_die()
        if (checkWinner(rolls) == True):
            winners += 1
    print(winners)
    print(winners / ITERATIONS) 
    

main()


