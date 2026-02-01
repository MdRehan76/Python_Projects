import random 

print("--------Guess the Number Game-----------")
def number_game():
    a = int(input("Enter the lower limit = "))
    b = int(input("Enter the upper limit = "))

    if a > b: 
        print("Lower limit cannot be greater than upper limit")
        exit()
    elif a == b:
        print('Lower Limit and Upper cannot be same ')
        exit()

    target_num = random.randint(a,b)

    print(f"Guess the Number between {a} to {b}")
    while True:
        x = input("Enter the number or Quit(Q) = ")
        if x.upper() == "Q":
            return False
        try:
            x = int(x)
        except ValueError:
            print(f"Invalid Input !...Please enter the valid integer between {a} to {b}")
            continue

        if x > target_num:
            print("Target number is smaller than your Guess number")
        elif x < target_num:
            print("Target number is greater than your Guess number ")
        else:
            print(f"Congrats!...\nYou guess the correct Target Number = {target_num}")
            return True
        
while True:
    result = number_game()
    if result:
        play = input(" Do you want to play again? (Y/N) = ")
        if play.upper() == "N":
            break
        elif play.upper() == "Y":
            continue
        else:
            print("Invalid input!..")
            break
    else:
        break

print("Thank you for playing!...")

