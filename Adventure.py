
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on dirt road, it has come to an end and u can go left or right. Which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? (walk/swim) ")

    if answer == "swim":
        print("You swam acrross and were aeten by an alligator.")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and died.")

    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back)")

    if answer == "back":
        print("You went back to the main road and along the way you got ambushed by bandits and you died.")

    elif answer == "cross":
        answer = input("You cross the bridge and met a stranger.Do you want to talk to them.? (yes/no)")
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")

        elif answer == "no":
            print("You ignored the stranger and they are offended so they killed you. ")

        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying " + name + "!")

quit()