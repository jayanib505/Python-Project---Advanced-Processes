##
# AS 91897 - Advanced Processes
# Jayani Bhula
# 30/07/2026

# Irish Learning Python Program
"""This program helps you learn Irish.

It lets the user:
    learn everyday greetings
    learn filler words
    learn with multiple choice questions
    view vocabulary of topics
    see points
    see your rank
    quit program.
"""
import random

# Welcome user
print("\nDia duit Kenish8")

# Topics available
print("""\nTopics:
  Everyday greetings (eg)
  Filler Words (fw)""")


def learn(topic, points, eg_questions, fw_questions, errors):
    """Ask multiple choice questions for selected topic."""
    # Variable that tracks lesson points and errors
    lesson_points = 0
    lesson_errors = 0

    # If Everyday greetings chosen set as vocabulary
    if topic == "eg":
        # Welcome User
        print("\nLearn Everyday greetings")

        # For Loop that runs through eg_questions
        for questions in eg_questions:
            # Prints out in multiple choice format
            print("""\nSelect the correct translation for: {}
            \nOptions: \n1.{} \n2.{} \n3.{}"""
                  .format(questions['Word'], questions['Answer'].title(),
                          questions['Options'][0], questions['Options'][1]))

            # Repeat until valid input entered
            while True:
                try:
                    # Get user answer selection
                    user_selection = int(input("Enter number selection: "))
                    # Check user input between range 1 and 3
                    if 1 <= user_selection <= 3:
                        break
                    # Instruct user to enter within range
                    print("Please enter 1, 2, or 3.")

                except ValueError:
                    # Tell user the input error
                    print("Enter a NUMBER (e.g 2) not letters ")

            # User write translation in English
            english_word = input("Write the translation for {}: "
                                 .format(questions['Word'])).strip().lower()

            # Check if answer is correct
            if user_selection == 1 and english_word == questions['Answer']:
                print("""Correct!
                Word added to vocabulary!""")
                lesson_points += 2     # Add 2 points

            else:
                # Shows user correct answer if they got question incorrect
                print("Incorrect. The answer was: {}"
                      .format(questions['Answer'].title()))
                lesson_errors += 1      # Add 1 error

    elif topic == "fw":
        # Welcome User
        print("\nLearn Filler Words")

        # For Loop that runs through eg_questions
        for questions in fw_questions:
            # Prints out in multiple choice format
            print("""\nSelect the correct translation for: {}
            \nOptions: \n1.{} \n2.{} \n3.{}"""
                  .format(questions['Word'], questions['Answer'].title(),
                          questions['Options'][0], questions['Options'][1]))

            while True:
                try:
                    # Get user answer selection
                    user_selection = int(input("Enter number selection: "))
                    # Check user input between range 1 and 3
                    if 1 <= user_selection <= 3:
                        break
                    # Instruct user to enter within range
                    print("Please enter 1, 2, or 3.")

                except ValueError:
                    # Tell user the input error
                    print("Enter a NUMBER (e.g 2) not letters ")

            # User write translation in English
            english_word = input("Write the translation for {}: "
                                 .format(questions['Word'])).strip().lower()

            # Check if answer is correct
            if user_selection == 1 and english_word == questions['Answer']:
                print("""Correct!
                Word added to vocabulary!""")
                lesson_points += 2     # Add 2 points

            else:
                # Shows user correct answer if they got question incorrect
                print("Incorrect. The answer was: {}"
                      .format(questions['Answer'].title()))
                lesson_errors += 1      # Add 1 error

    # Print Lesson stats
    print("\n---Lesson Stats---")
    print("You have earned {} points!".format(lesson_points))

    # Prints error outcome with correct grammar
    if lesson_errors == 1:
        print("{} error was made.".format(lesson_errors))
    else:
        print("{} errors were made.".format(lesson_errors))

    # Return values back with lesson points and errors added
    return points + lesson_points, errors + lesson_errors


def vocabulary(everyday_greetings, filler_words):
    """Print vocabulary for chosen topic."""
    print("\nWelcome to the Vocabulary")

    # Topics available
    print("""\nTopics:
  Everyday greetings (eg)
  Filler Words (fw) """)

    # Ask user for topic
    topic = input("\nEnter vocab topic: ").strip().lower()

    if topic == "eg":
        print("\nVocab  -  Everyday greetings")
        # For loop prints formatted vocabulary
        for basic in everyday_greetings:
            print("{:13} | {:15}".format(basic['English'], basic['Irish']))

    elif topic == "fw":
        print("\nVocab  -  Filler Words")
        # For loop prints formatted vocabulary
        for filler in filler_words:
            print("{:5} | {:15}".format(filler['English'], filler['Irish']))


def profile(points, errors):
    """Display user learning stats."""
    print("\nWelcome to Profile")
    print("Username: Kenish8")

    # Determine rank based off points
    if points <= 10:
        print("Rank: Rookie")

    elif 11 <= points <= 30:
        print("Rank: Sophomore")

    elif 31 <= points <= 40:
        print("Rank: Pro")

    elif 41 <= points <= 50:
        print("Rank: Veteran")

    else:
        print("Rank: Legend")

    # Print current points
    print("Points: {}".format(points))
    # Print errors
    print("Errors: {}".format(errors))


def main():
    """Menu and holds word lists."""
    # List of ditionaries containing word, answer and options
    eg_questions = [
            {"Word": "Haigh", "Answer": "hi",
             "Options": ["Hello", "Bye"]},
            {"Word": "Dia duit", "Answer": "hello",
             "Options": ["Bye", "Please"]},
            {"Word": "Slán", "Answer": "bye",
             "Options": ["Thankyou", "Please"]},
            {"Word": "Le do thoil", "Answer": "please",
             "Options": ["Welcome", "Hi"]},
            {"Word": "Go raibh maith agat", "Answer": "thankyou",
             "Options": ["Welcome", "Bye"]},
            {"Word": "Maidin mhaith", "Answer": "good morning",
             "Options": ["Hello", "Welcome"]},
            {"Word": "Fáilte", "Answer": "welcome",
             "Options": ["Bye", "Please"]},
            ]
    # List of ditionaries containing word, answer and options
    fw_questions = [
        {"Word": "Le", "Answer": "with", "Options": ["And", "Or"]},
        {"Word": "Agus", "Answer": "and", "Options": ["With", "The"]},
        {"Word": "No", "Answer": "or", "Options": ["The", "And"]},
        {"Word": "An", "Answer": "the", "Options": ["With", "Or"]}
        ]

    # List of dictionaries - Topic: Everyday greetings
    everyday_greetings = [
        {"English": "Hi", "Irish": "Haigh"},
        {"English": "Hello", "Irish": "Dia Duit"},
        {"English": "Bye", "Irish": "Slán"},
        {"English": "Please", "Irish": "Le do thoil"},
        {"English": "Thankyou", "Irish": "Go raibh maith agat"},
        {"English": "Welcome", "Irish": "Fáilte"},
        {"English": "Good Morning", "Irish": "Maidin mhaith"}
        ]

    # List of dictionaries - Topic: Filler Words
    filler_words = [
        {"English": "With", "Irish": "le"},
        {"English": "And", "Irish": "agus"},
        {"English": "Or", "Irish": "no"},
        {"English": "The", "Irish": "an"}
        ]

    # Points variable
    points = 0

    # Errors variable
    errors = 0

    # Loop
    while True:
        # Menu
        print("\n")
        print("\n---Dashboard---")
        print("1. Profile")
        print("2. Vocabulary")
        print("3. Learn")
        print("0. Exit")

        # Ask for option choice
        decision = input("\nEnter number option: ")

        if decision == "1":
            # User profile function
            profile(points, errors)

        elif decision == "2":
            # Vocabulary function
            vocabulary(everyday_greetings, filler_words)

        elif decision == "3":
            print("\nWelcome to Learn")
    
            print("""\nTopics:
    Everyday greetings (eg)
    Filler Words (fw) """)
      
            # Ask user for topic input
            topic = input("\nEnter topic to learn: ").strip().lower()

            if topic == "eg":
                # Stores returned points
                points, errors = learn(topic, points,
                                       eg_questions, fw_questions, errors)
                
            elif topic == "fw":
                # Stores returned points
                points, errors = learn(topic, points, 
                                       eg_questions, fw_questions, errors)

        elif decision == "0":
            print("""\n\nFantastic job today,
            see you tomorrow to continue learning Irish!""")
            print("\nTotal points: {}"
                  .format(points))  # Prints user total points

            # Random choice selects a word from either dictionary
            remember_word = random.choice(everyday_greetings + filler_words)
            # Prints out chosen word in formatted statement
            print("Task: Remember | {} ({}) for next time!"
                  .format(remember_word['Irish'].title(), remember_word['English']))

            # Goodbye to user
            print("\nSlán go fóill! (Goodbye for now!)")

            # Message indicating program ending
            print("Session over.")
            break   # Exits loop

        else:
            print("Invalid input.")


if __name__ == "__main__":

    main()

