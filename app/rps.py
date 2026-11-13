import random

VALID_OPTIONS = ["rock", "paper", "scissors"]

user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ").lower()
print(f"USER CHOICE: {user_choice}")

if user_choice not in VALID_OPTIONS:
	print("OOPS, INVALID CHOICE. PLEASE TRY AGAIN.")
	exit()

computer_choice = random.choice(VALID_OPTIONS)
print(f"COMPUTER CHOICE: {computer_choice}")

if user_choice == computer_choice:
	print("TIE GAME!")
elif user_choice == "rock" and computer_choice == "paper":
	print("COMPUTER WINS!")
elif user_choice == "rock" and computer_choice == "scissors":
	print("COMPUTER WINS!")  # Intentional bug for assignment
elif user_choice == "paper" and computer_choice == "rock":
	print("USER WINS!")
elif user_choice == "paper" and computer_choice == "scissors":
	print("COMPUTER WINS!")
elif user_choice == "scissors" and computer_choice == "rock":
	print("COMPUTER WINS!")
elif user_choice == "scissors" and computer_choice == "paper":
	print("USER WINS!")
