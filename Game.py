##########################
##Rock-paper-scissors-###
##########################

from enum import IntEnum
import random


class Action(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3

    def user_action(self):
        choice = int(input("Enter your Choice: [1] for rock /n [2] for paper /n [3] for scissors: "))
        if (choice > 3):
            print("size error !! must be  less then 3,Try Again")
            return self.user_action()
        else:
            a = Action(choice)
            return (a)

    def comp_action(self):
        choice = random.randint(0, len(Action))
        a = Action(choice)
        return a

    def determine_winner(user_action, comp_action):
        victories = {
            Action.Rock: [Action.Scissors],
            Action.Paper: [Action.Rock],
            Action.Scissors: [Action.Paper]
        }

        defeats = victories[user_action]
        if user_action == comp_action:
            print(f"Both players selected {user_action.name}. It's a tie!")
        elif comp_action in defeats:
            print(f"{user_action.name} beats {comp_action.name}! You win!")
        else:
            print(f"{comp_action.name} beats {user_action.name}! You lose.")


x = Action.user_action(0)
y = Action.comp_action(0)

a = Action.determine_winner(x, y)
