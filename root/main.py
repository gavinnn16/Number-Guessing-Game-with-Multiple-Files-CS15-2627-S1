from utils import *
from score import *

secret_number = generate_secret_number()
player_score = 100

while True:
    if check_user_guess(secret_number):
        print(f"\nFinal Score: {player_score}")
        print(f"Rating: {get_rating(player_score)}")
        break
    else:
        player_score = calculate_new_score(player_score)