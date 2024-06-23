import random

ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['C', 'D', 'H', 'S']



#H = ["10"]
#a = ['a10', 'cK']
#print(len(a[0]))
#print(a[0][1:3] in H)

face = ['J', 'Q', 'K']
point = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
ace = ["A"]




def card_value(card):#compute card value
	card_value = 0
	ace_num = 0
	for i in range(len(card)):# considering 10 ACE JQK
		if len(card[i]) == 3:
			value = card[i][1:3]
			if value in face:
				value = 10
			elif value in ace:
				value = 11
				ace_num += 1
			else:
				value = int(value)
		elif len(card[i]) == 2:
			value = card[i][1]
			if value in face:
				value = 10
			elif value in ace:
				value = 11
				ace_num += 1
			else:
				value = int(value)

		card_value=card_value+value
		#print(card_value)
	if ace_num>0:
		for k in range(ace_num+1):
			if(card_value>21):
				card_value=card_value-10
			return card_value	
	else:
		return card_value

#print(player_card)
#print(card_value(player_card))
#print(card_value(dealer_card))
#test=['c9','cK','c5']
#print(card_value(test))
def print_last_card(card): #print the card you draw
	print("with the hand: ",end="")
	out_num=0
	out_color=0
	if len(card)==3:
			out_num=card[1:3]
	else:
		if card[1]=='J':
			out_num='JACK'
		elif card[1]=='Q':
			out_num='QUEEN'
		elif card[1]=='K':
				out_num='KING'
		elif card[1]=='A':
				out_num='ACE'
		else:
				out_num=card[1]
	if card[0]=='C':
			out_color='CLUB'
	elif card[0]=='D':
			out_color='DIAMOND'
	elif card[0]=='H':
			out_color='HEART'
	elif card[0]=='S':
			out_color='SPADE'
	print(out_num,"-",out_color,",",end="")		
	print()	

def print_card(card):#print the cards your in hand
	print("with the hand: ",end="")
	out_num=0
	out_color=0
	for i in range(len(card)):
		if len(card[i])==3:
			out_num=card[i][1:3]
		else:
			if card[i][1]=='J':
				out_num='JACK'
			elif card[i][1]=='Q':
				out_num='QUEEN'
			elif card[i][1]=='K':
				out_num='KING'
			elif card[i][1]=='A':
				out_num='ACE'
			else:
				out_num=card[i][1]
		if card[i][0]=='C':
			out_color='CLUB'
		elif card[i][0]=='D':
			out_color='DIAMOND'
		elif card[i][0]=='H':
			out_color='HEART'
		elif card[i][0]=='S':
			out_color='SPADE'
		print(out_num,"-",out_color,",",end="")
	print()	


win_or_lose=0

while (win_or_lose==0):# largest loop to provide restart the game
	deck = [] 
	for s in suits:
		for r in ranks:
			deck.append(s+r)
	random.shuffle(deck)


	player_card = []
	dealer_card = []
	for i in range(2):
		player_card.append(deck.pop(0))
		dealer_card.append(deck.pop(0))
	#randomly shuffle the card

	user_hit=1
	#print(player_card)
	print("Your current value = ",card_value(player_card))
	print_card(player_card)

	while (user_hit==1):#for user/dealer to hit 
		print()
		user=input("Hit or stay? (Hit = 1 , Stay = 0): ")
		print()
		user_hit=int(user)
		if user_hit==0:
			break
		last_card=deck.pop(0)
		player_card.append(last_card)
		print()
		print("You draw ", end="")
		print_last_card(last_card)
		print()
		#print(player_card)
		print("Your current value = ",card_value(player_card))
		print_card(player_card)
		if card_value(player_card)>21:
			break
	if card_value(player_card)>21:#>21 is dead
		print("*** Dealer wins! ***")
		win_or_lose=1
	else:	
		dealer_hit=1
		#print(dealer_card)
		print("Dealer current value = ",card_value(dealer_card))
		print_card(dealer_card)
		while (dealer_hit==1):
			if card_value(dealer_card)<18:
				dealer_hit=1
				last_card=deck.pop(0)
				dealer_card.append(last_card)
				print()
				print("Dealer draws ", end="")
				print_last_card(last_card)
				print()
				#print(dealer_card)
				print("Dealer current value = ",card_value(dealer_card))
				print_card(dealer_card)
			else:
				dealer_hit=0
			if card_value(player_card)>21:#>21 is dead
				break
		if card_value(dealer_card)>21:
			print("*** You beat the dealer! ***")
			win_or_lose=1
			
		elif card_value(player_card)>card_value(dealer_card):
			print("*** You beat the dealer! ***")
			win_or_lose=1
			
		elif card_value(player_card)<card_value(dealer_card):
			print("*** Dealer wins! ***")
			win_or_lose=1
		elif card_value(player_card)==card_value(dealer_card):
			print("*** Dealer wins! ***")
			win_or_lose=1
		#determines who wins
	if win_or_lose==1:
		again=input("Want to play again? (y/n)")
		if again=='y':
			win_or_lose=0
		else:
			win_or_lose=1



	


	

