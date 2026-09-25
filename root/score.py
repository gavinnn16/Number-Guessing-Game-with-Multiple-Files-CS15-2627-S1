
current_score = 100
def update_score(current_score):
    new_score = current_score - 10
    return max(0, new_score)
def get_rating(final_score):
   if final_score >= 80:
       return "Wow your a genius you scored a Excellent"
   elif final_score >= 50:
       return "Hey its alright with a little practice you will be perfect you scored a Good"
   else:
       return "Woah maybe your not fit for this game you scored a Poor"
if __name__ == "__main__":
    test_score = 100
    print(f"Starting Score {test_score}")
    test_score = update_score(test_score)
    print(f"WRONG {test_score}")

    print("Ratings")
    print(f"{get_rating(85)}")
    print(f"{get_rating(50)}")
