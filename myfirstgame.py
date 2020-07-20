print("Welcome to my first game")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "your are", age, "years old")

health = 10
print("You are starting with", health, "health")

if age >= 18:
    print("You are old enough to play!")
    wanna_play = input("Do you want to play? ").lower()
    if wanna_play == "yes":
        print("Let's play")
        left_or_right = input("First choice: Left or Right(left/right)?").lower()
        if left_or_right == "left":
            ans = input(
                "Nice, you are following the path and reach a lake... You you swim across or go around(across/around)?").lower()
            if ans == "around":
                print("You went around and reached the other side of the lake")

            elif ans == "across":
                print("You managed to get across and were bit by a fish and lost 5 health")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to (house/river)? ")
            if ans == "house":
                print("You go to the house and are greeted by the owner. he does not like you and you lose 5 health")
                health -= 5
                if health <= 0:
                    print("You have 0 health and you lost!")
                else:
                    print("You have survived and win ")

            else:
                print("You fell in the river and lost")

        else:
            print("You fell down and lost ...")
    else:
        print("See you next time")
elif age >= 14:
    print("You can play with supervision")
else:
    print("You are not old enough!")


