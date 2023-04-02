import random, time


def count_down():
    for i in range(3, 0, -1):
        time.sleep(1)
        print(i)

def exit():
    print("Game is closing...")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)

def start_message():
    print("Game is Starting...")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    start_game()

def start_game(number_prediction = 5):

    print("**Number prediction game is about to start**")
    print("!! Don't forget: You have 5 predictions !!")

    count_down()

    correct_number = random.randrange(0,100)


    while (number_prediction>0):
        prediction = int(input("I have chosen a number between 0-100 in my mind (It cannot be 100). What do you think this number is? : "))

        if (prediction < correct_number):
            number_prediction -= 1
            if (number_prediction==0):
                break

            print("Ascend your prediction!")
        elif (prediction > correct_number):
            number_prediction -= 1
            if (number_prediction==0):
                break
            print("Descend your prediction!")
        else:
            print("Congratulations! You got the correct number :) ")
            print("The number I have chosen was", correct_number,".")
            break

    if (number_prediction==0):
        print("Your prediction is wrong!")
        print("You have no prediction left :( ")
        print("The number I have chosen was", correct_number,".")

    again = input("Do you want to play again? Y / N : ")

    if (again =="Y"):
        start_message()
    else:
        exit()

start_game()