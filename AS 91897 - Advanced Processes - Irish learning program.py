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

# Welcome user
print("\nDia duit Kenish8")

# Topics available
print("""\nTopics:
  Everyday greetings (eg)
  Filler Words (fw)""")


def learn(topic, points, eg_questions, fw_questions):
    """Ask multiple choice questions for selected topic."""
    # If Everyday greetings chosen set as vocabulary
    if topic == "eg":
        # Welcome User
        print("\nLearn Everyday greetings")

        # For Loop that runs through eg_questions
        for questions in eg_questions:
            print("""\nSelect the correct translation for:
                  {} \n \nOptions: \n1.{} \n2.{} \n3.{}"""
                  .format(questions['Word'], questions['Answer'].title(),
                          questions['Options'][0], questions['Options'][1]))

            # Repeat until valid input entered
            while True:
                try:
                    # Get user answer selection
                    user_selection = int(input("Enter number selection: "))
                    break

                except ValueError:
                    # Tell user the input error
                    print("Enter a NUMBER (e.g 2) not letters ")

            # User write translation in English
            english_word = input("Write the translation for {}: "
                                 .format(questions['Word'])).strip().lower()

            # Check if answer is correct
            if user_selection == 1 and english_word == questions['Answer']:
                print("""Correct!
                Congratulations on learning a new word!""")
                points += 2     # Add 2 points

            else:
                print("Incorrect. The answer was: {}"
                      .format(questions['Answer'].title()))

    elif topic == "fw":
        # Welcome User
        print("\nLearn Filler Words")

        # For Loop that runs through eg_questions
        for questions in fw_questions:
            print("""\nSelect the correct translation for:
                  {} \n \nOptions: \n1.{} \n2.{} \n3.{}"""
                  .format(questions['Word'], questions['Answer'].title(),
                          questions['Options'][0], questions['Options'][1]))

            while True:
                try:
                    # Get user answer selection
                    user_selection = int(input("Enter number selection: "))
                    break

                except ValueError:
                    # Tell user the input error
                    print("Enter a NUMBER (e.g 2) not letters ")

            # User write translation in English
            english_word = input("Write the translation for {}: "
                                 .format(questions['Word'])).strip().lower()

            # Check if answer is correct
            if user_selection == 1 and english_word == questions['Answer']:
                print("""Correct!
                Congratulations on learning a new word!""")
                points += 2     # Add 2 points

            else:
                print("Incorrect. The answer was: {}"
                      .format(questions['Answer'].title()))

    return points


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


def profile(points):
    """Display user learning stats."""
    print("\nWelcome to Profile")
    print("Username: Kenish8")

    # Determine rank based off points
    if points < 10:
        print("Rank: Rookie")

    elif 10 <= points <= 30:
        print("Rank: Sophomore")

    elif 30 < points <= 40:
        print("Rank: Pro")

    elif 40 < points <= 50:
        print("Rank: Veteran")

    else:
        print("Rank: Legend")

    # Print current points
    print("Points: {}".format(points))


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

    # Loop
    while True:
        # Menu
        print("\n")
        print("\n---Dashboard---")
        print("1. Learn")
        print("2. Vocabulary")
        print("3. Profile")
        print("0. Exit")

        # Ask for option choice
        decision = input("\nEnter number option: ")

        if decision == "1":
            print("\nWelcome to Learn")

            print("""\nTopics:
  Everyday greetings (eg)
  Filler Words (fw) """)

            # Ask user for topic input
            topic = input("\nEnter topic to learn: ").strip().lower()
            if topic == "eg":
                # Stores returned points
                points = learn(topic, points, eg_questions, fw_questions)

            elif topic == "fw":
                # Stores returned points
                points = learn(topic, points, eg_questions, fw_questions)

        elif decision == "2":
            # Vocabulary function
            vocabulary(everyday_greetings, filler_words)

        elif decision == "3":
            # User profile function
            profile(points)

        elif decision == "0":
            # Message indicating program ending
            print("Session over.")
            break   # Exits loop


if __name__ == "__main__":

    main()

