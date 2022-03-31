from game_data import data
from art import logo
from art import vs
import random


def compare():
    if choice_a['follower_count'] > choice_b['follower_count']:
        return choice_a
    elif choice_b['follower_count'] > choice_a['follower_count']:
        return choice_b


print(logo)
choice_a = random.choice(data)
print(f"Compare A: {choice_a['name']}, {choice_a['description']}, {choice_a['country']}")
print(vs)
choice_b = random.choice(data)
print(f"Against B: {choice_b['name']}, {choice_b['description']}, {choice_b['country']}")

game_on = True
score = 0

while game_on:
    popular = compare()
    guess = input("Who has more follower? Type 'a' or 'b': ")
    print(logo)
    if guess == 'a':
        guess = choice_a
    else:
        guess = choice_b
    if guess == popular:
        score += 1
        print(f"Your Right!! Current Score: {score}")
        choice_a = guess
        print(f"Compare A: {choice_a['name']}, {choice_a['description']},{choice_a['country']}")
        print(vs)
        choice_b = random.choice(data)
        print(f"Against B: {choice_b['name']}, {choice_b['description']}, {choice_b['country']}")

    else:
        print("You Lose!!")
        print(f"Your Score Was {score}")
        game_on = False
