
current_score = 100
def update_score(current_score):
    new_score = current_score - 10
    if new_score < 0:
        return 0
def get_rating(final_score):
   if final_score >= 80:
       return "Excellent"
   elif final_score >= 50:
       return "Good"
   else:
       return "Keep Practicing"
if __name__ == "__main__":
    test_score = 100
    print(f"Starting Score {test_score}")
    test_score = update_score(test_score)
    print(f"WRONG {test_score}")

    print("Ratings")
    print(f"{get_rating(85)}")
    print(f"{get_rating(50)}")