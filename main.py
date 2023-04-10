#from replit import clear
import random
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_cards_sum = 0
user_cards_sum = 0

def new_game():
	ask = input("Do you want to play a game of Blackjack? Type 'y' for yes, 'n' for no: ").lower()
	if ask == 'y':
		#clear()
		print(logo)
		black_jack()
		new_game()
		
def black_jack():
	should_continue = True
	while should_continue:
		user_cards = random.sample(cards, 2)
		computer_cards = random.sample(cards, 2)
		user_cards_sum = sum(user_cards)
		computer_cards_sum = sum(computer_cards)


		
		def message():
			print(f"  Your cards: {user_cards} current score: {user_cards_sum}")
			print(f"  Computer's first card: {computer_cards[0]} ")
		
		def final_message():
			print(f"Your final hand: {user_cards}, current score: {user_cards_sum}")
			print(f"Computer's final hand: {computer_cards}, current score: {computer_cards_sum}")


			
		message()
		while sum(computer_cards) < 17:
			computer_cards += random.sample(cards, 1)
			computer_cards_sum = sum(computer_cards)
	
		if computer_cards_sum > 21:
			for x in range(len(computer_cards)):
				if computer_cards[x] == 11:
					computer_cards_sum = sum(computer_cards) - 10
			
		get_card = True
		if user_cards_sum == 21:
			print("Win with a Blackjack 😎")
			get_card = False
			should_continue = False
			
		if computer_cards_sum == 21 and len(computer_cards) == 2:
			print(f"Computer's final hand {computer_cards}")
			print("Lose, opponent has Blackjack 😱")
			get_card = False
			should_continue = False
		while get_card:
			ask_to_get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
			
			if ask_to_get_card == "y":
				user_cards += random.sample(cards, 1)
				user_cards_sum = sum(user_cards)
				
				if user_cards_sum > 21:
					for x in range(len(user_cards)):
						if user_cards[x] == 11:
							user_cards_sum -= 10
			elif ask_to_get_card == 'n':
				get_card = False
				
			message()
			compare = True
			if user_cards_sum > 21:
				final_message()
				print("You went over. You lose 😭")
				get_card = False
				should_continue = False
				compare = False 			
					
				
			
			if computer_cards_sum > 21:
				final_message()
				print("Opponent went over. You win 😁")
				get_card = False
				compare = False

		while compare == True:		
			if abs(user_cards_sum - 21) > abs(computer_cards_sum - 21) and should_continue:
				final_message()
				print("You lose 😤")
				should_continue = False
			elif abs(user_cards_sum - 21) == abs(computer_cards_sum - 21) and should_continue:
				final_message()
				print("Draw 🙃")
				should_continue = False
			elif abs(user_cards_sum - 21) < abs(computer_cards_sum) and should_continue:
				final_message()
				print("You win 😃")
				should_continue = False

new_game()