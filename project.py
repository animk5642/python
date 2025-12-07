name = input("Enter Your Name here:")
print("hi", name, "welcome to the game")

should_play = input("do you need to play").lower()

play = not (should_play == "yes" or should_play == "y")


if play == False:
    print("lets paly")
    direction = input("enter which direction(left/right) ")
    if direction == "left":
        print("move left")
    elif direction == "right":
        print("move right")
    else:
        print("nodirection ")

else:
    print("cannot play")
