def run_quiz():
    score = 0
    total_questions = 5

    print("==========================================")
    print(" WELCOME TO THE ULTIMATE GEOMETRY DASH ")
    print(" TERMINAL QUIZ ")
    print("==========================================\n")

    # Question 1
    q1 = input("1. What modding utility is widely used in Geometry Dash for custom mods and utilities?\n> ")
    if q1.strip().lower() == "geode":
        print("Correct! +1 point\n")
        score += 1
    else:
        print("Incorrect! The answer is Geode.\n")

    # Question 2
    q2 = input("2. What difficulty rating sits right above Hard Demon?\n> ")
    if q2.strip().lower() in ["insane demon", "insane"]:
        print("Correct! +1 point\n")
        score += 1
    else:
        print("Incorrect! The answer is Insane Demon.\n")

    # Question 3
    q3 = input("3. What term is used for bypassing the game's frame rate limit for smoother physics?\n> ")
    if "fps" in q3.strip().lower() or "tps" in q3.strip().lower():
        print("Correct! +1 point\n")
        score += 1
    else:
        print("Incorrect! (FPS/TPS bypass)\n")

    # Question 4
    q4 = input("4. True or False: Do community levels feature songs from Newgrounds?\n> ")
    if q4.strip().lower() in ["true", "t", "yes"]:
        print("Correct! +1 point\n")
        score += 1
    else:
        print("Incorrect! They use Newgrounds tracks.\n")

    # Question 5 (Boss Level)
    q5 = input("5. What legendary top one Extreme Demon was verified on August 12, 2015?\n> ")
    if q5.strip().lower() == "bloodbath":
        print("Correct! Absolute legend status. +1 point\n")
        score += 1
    else:
        print("Incorrect! The answer was Bloodbath.\n")

    # Final Score
    print("==========================================")
    print(f" Quiz complete! Your final score: {score}/{total_questions}")
    print("==========================================")

if __name__ == "__main__":
    run_quiz()

