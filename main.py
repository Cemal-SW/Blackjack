




#If computer cards total is less than 17, computer picks another card from the deck
#Calculate the score
#Show the 2 cards of user and 1 card of computer
#Ask user if they want's another card, if user score > 21 => don't ask again
#Calculate and show the current situation everytime user gets card
#Check for other conditions to decide who wins
#Print the appropriate message for true condition

import random
from art import logo
import os
clear = lambda: os.system('cls')

def choose_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card

def check_for_blackjack(cards_list):
	if sum(cards_list) == 21 and len(cards_list) == 2:
		return True
		 
def check_who_wins(user_cards_sum, computer_cards_sum, user_has_blackjack, computer_has_blackjack):
	if user_cards_sum > 21 and computer_cards_sum > 21:
		return "You went over. You lose 😤"
	if user_cards_sum > 21: 
		return "You went over. You lose 😭"
	elif user_cards_sum == computer_cards_sum:
		return "Draw 🙃"
	elif user_has_blackjack:
		return "Win with a Blackjack 😎"
	elif computer_has_blackjack:
		return "Lose, opponent has Blackjack 😱"
	elif abs(user_cards_sum - 21) < abs(computer_cards_sum - 21):
		return "You win 😃"
	elif abs(user_cards_sum - 21) > abs(computer_cards_sum - 21):
		return "You lose 😤"
	

def cards_sum(card_list):
	total = sum(card_list)
	if total > 21:
		for x in range(len(card_list)):
			if x == 11:
				total -= 10

	if sum(card_list) == 21 and len(card_list) == 2:
		return 0
	
	return total

def blackjack_game():

	print(logo)
	user_cards = []
	computer_cards = []
	game_over = False

	#Choose two cards for both the computer and the user
	for x in range(2):
		user_cards.append(choose_card())
		computer_cards.append(choose_card())
	#Calculate the score
	user_cards_sum = cards_sum(user_cards)
	computer_cards_sum = cards_sum(computer_cards)

	#Check if there is a blackjak condition with using len of the cards, if so ends the game.
	#Returns 'blackjack' if there is a blackjack condition
	user_has_blackjack = check_for_blackjack(user_cards)
	computer_has_blackjack = check_for_blackjack(computer_cards)

	if computer_cards_sum < 17:
		computer_cards.append(choose_card())
		computer_cards_sum = cards_sum(computer_cards)
	
	while game_over == False:
		
		print(f"   Your cards: {user_cards}, current score: {user_cards_sum}")
		print(f"   Computer's first card: {computer_cards[0]}")

		if user_has_blackjack or computer_has_blackjack or user_cards_sum > 21:
			game_over = True
		else:
			ask = input("Type 'y' to get another card, type 'n' to pass: ").lower()

			if ask == 'y':
				user_cards.append(choose_card())
				user_cards_sum = sum(user_cards)
			elif ask == 'n':
				
				game_over = True

	print(f"   Your final hand: {user_cards}, final score: {user_cards_sum}")
	print(f"   Computer's final hand: {computer_cards}, final score: {computer_cards_sum}")
	print(check_who_wins(user_cards_sum, computer_cards_sum, user_has_blackjack, computer_has_blackjack))	


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
	clear()
	blackjack_game()
else:
	print("The game has ended.")