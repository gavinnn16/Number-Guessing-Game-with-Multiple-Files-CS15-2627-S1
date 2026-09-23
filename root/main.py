from utils import generate_secret_number, check_user_guess
from score import update_score, get_rating

secret_number = generate_secret_number()
player_score = 100

while True:
    if check_user_guess(secret_number):
        print(f"\nFinal Score: {player_score}")
        print(f"Rating: {get_rating(player_score)}")
        break
    else:
        player_score = update_score(player_score)