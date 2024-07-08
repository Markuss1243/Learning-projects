import random
# input 2 numbers to create a range
# randomly generate a number in the range

def randomrange():
    print("Please input the minimum number:")
    number1 = int(input())
    print("Please input the maximum number:")
    number2 = int(input())
    x = random.randint(int(number1),int(number2))
    # delete print when done
    # print(x)
    return x
    
# guess generated number1
def guess(x):
    print("Please Guess the Number:")
    guessnumber = int(input())
    #if guessnumber == int(x):
        #print("Well Done")
    if guessnumber > x:
        print("The number is lower!")
        return 1
    elif guessnumber < x:
        print("The number is higher!")
        return 1
    else:
        print("Well Done")
        return 0


def main():
    x = randomrange()
    print(x)
    totalchances = 2 #random.randint(1,10)
    chances = 0
    while chances < totalchances:
        guessr = guess(x)
        chances += guessr
        if guessr == 0:
            return 0
        if chances == totalchances:
            print(f'Your guess was {guessr}.')
            print(f'The number was {x}.')
        print(f'You have {totalchances - chances}/{totalchances} left.')
        # delete print guessr
        
main()

# higher, lower or correct depending on guess
# limit guess amount after which a fail message pops up




    
