
def calculate_new_score(current_score):
    new_score = current_score - 10
    if new_score < 0:
        new_score = 0
    return new_score

def get_rating(final_score):
   if final_score >= 80:
       return "Wow your a genius you scored a Excellent"
   elif final_score >= 50:
       return "Hey its alright with a little practice you will be perfect you scored a Good"
   else:
       return "Woah maybe your not fit for this game you scored a Poor"
if __name__ == "__main__":
    print(calculate_new_score(100))
    print(calculate_new_score(5))

    print(get_rating(80))
    print(get_rating(50))
    print(get_rating(30))