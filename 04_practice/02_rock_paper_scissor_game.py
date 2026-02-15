import random
computer = random.randint(1,3)
print(computer)
user = int(input("Enter 1 for rock, 2 for paper, 3 for scissor: "))
match (user,computer):
    case (user,computer) if user == computer:
        print("It's a tie")
    case (1,3) | (2,1) | (3,2):
        print("You win")
    case _:
        print("Computer wins")