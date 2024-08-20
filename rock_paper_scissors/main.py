import random as rd
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

object_graphs = [rock, paper, scissors]
object_strings = ["rock", "paper", "scissors"]

print("Welcome To our beautiful game of rock/paper/scissors")
chosen_object = input("Choose one object: rock/paper/scissors \n")

while True:
    try:
        user_index = object_strings.index(chosen_object)
        break
    except ValueError:
        chosen_object = input("You made a typo. Choose one object: rock/paper/scissors \n")
        continue

user_graph = object_graphs[user_index]
print("User chose:")
print(user_graph)

computer_index = rd.randint(0, len(object_graphs) - 1)
computer_graph = object_graphs[computer_index]
print("Computer chose:")
print(computer_graph)


message = ""
message_details = f"\n-----\nYou chose {object_strings[user_index]}\nComputer chose {object_strings[computer_index]}\n"

if user_index > computer_index:
    if user_index == 2 and computer_index == 0:
        message = f"You Lose!"
    else:
        message = "You Win!"
elif user_index == computer_index:
    message = "Draw!"
else:
    if computer_index == 2 and user_index == 0:
        message = f"You Win!"
    else:
        message = "You Lose!"


print(message_details + message + "\n-----\n")