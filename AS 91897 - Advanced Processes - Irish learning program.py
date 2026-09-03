##
# AS 91897 - Advanced Processes
# Jayani Bhula
# 30/07/2026


# Welcome user
print("\nDia duit Kenish8\n")


print("""Topics:
Everyday greetings""")



def learn(everyday_greetings):
    """Ask multiple choice questions for selected topic"""
    print("\nWelcome to Learn")

    print("""\nTopics:
Everyday greetings\n""")

    topic = input("Enter topic to learn: ").title()
    while True:
        # If Everyday greetings chosen set as vocabulary
        if topic == "Eg":

            # Welcome User
            print("\nLearn Everyday greetings")

            # Select Irish translation
            print("\nSelect the correct translation for: Haigh")

            # English translation options
            print("1. Hello")
            print("2. Hi")
            print("3. Bye")

            # Get user answer selection
            user_selection = int(input("Enter number selection: "))
            # User write translation in English
            english_word = input("Write the translation for Haigh: ")

            # Check if selection correct
            if user_selection == 2 and english_word == "Hi":
                 print("""Correct.
                 Word added to vocabulary!""")

            elif user_selection == 0 or english_word == "0":
                break

            else:
                print("Incorrect. Keep going!")

            # Select Irish translation
            print("\nSelect the correct translation for: Dia duit")

            # English translation options
            print("1. Bye")
            print("2. Please")
            print("3. Hello")

            # Get user answer selection
            user_selection = int(input("Enter number selection: "))
            # User write translation in English
            english_word = input("Write the translation for Dia duit: ")   

            # Check if selection correct
            if user_selection == 3 and english_word == "Hello":
                print("""Correct.
                Word added to vocabulary!""")

            else:
                print("Incorrect. Keep going!")

            # Select Irish translation
            print("\nSelect the correct translation for: Slán")

            # English translation options
            print("1. Bye")
            print("2. Thank you")
            print("3. Please")

            # Get user answer selection
            user_selection = int(input("Enter number selection: "))
            # User write translation in English
            english_word = input("Write the translation for Slán: ")

            # Check if selection correct
            if user_selection == 1 and english_word == "Bye":
                print("""Correct.
                Word added to vocabulary!""")

            else:
                print("Incorrect. Keep going!")

            # Select Irish translation
            print("\nSelect the correct translation for: Le do thoil")

            # English translation options
            print("1. Hi")
            print("2. Welcome")
            print("3. Please")

            # Get user answer selection
            user_selection = int(input("Enter number selection: "))
            # User write translation in English
            english_word = input("Write the translation for Le do thoil: ")

            # Check if selection correct
            if user_selection == 3 and english_word == "Please":
                print("""Correct.
                Word added to vocabulary!""")

            else:
                print("Incorrect. Keep going!")

            # Select Irish translation
            print("\nSelect the correct translation for: Go raibh maith agat")

            # English translation options
            print("1. Thank you")
            print("2. Welcome")
            print("3. Bye")

            # Get user answer selection
            user_selection = int(input("Enter number selection: "))
            # User write translation in English
            english_word = input("Write the translation for Go raibh maith agat: ")

            # Check if selection correct
            if user_selection == 1 and english_word == "Thank you":
                print("""Correct.
                Word added to vocabulary!""")

            else:
                print("Incorrect. Keep going!")

            # Select Irish translation
            print("\nSelect the correct translation for: Maidin mhaith")

            # English translation options
            print("1. Hello")
            print("2. Good Morning")
            print("3. Welcome")

            # Get user answer selection
            user_selection = int(input("Enter number selection: "))
            # User write translation in English
            english_word = input("Write the translation for Maidin mhaith: ")

            # Check if selection correct
            if user_selection == 2 and english_word == "Good Morning":
                print("""Correct.
                Word added to vocabulary!""")

            else:
                print("Incorrect. Keep going!")

            # Select Irish translation
            print("\nSelect the correct translation for: Fáilte")

            # English translation options
            print("1. Bye")
            print("2. Please")
            print("3. Welcome")

            # Get user answer selection
            user_selection = int(input("Enter number selection: "))
            english_word = input("Write the translation for Fáilte: ")

            # Check if selection correct
            if user_selection == 3 and english_word == "Welcome":
                print("""Correct.
                Word added to vocabulary!!""")

            else:
                print("Incorrect. Keep going!")



def vocabulary(everyday_greetings):
    """Print vocabulary for chosen topic"""
    print("\nWelcome to the Vocabulary")

    # Ask user for topic
    topic = input("Enter vocab topic: ").title()

    if topic == "Eg":
        print("\nVocab  -  Everyday greetings")
        # For loop prints formatted vocabulary
        for basic in everyday_greetings:
            print("{:13} | {:15}".format(basic['English'], basic['Irish']))


def profile():
    """Display user learning stats"""
    print("Profile")


def main():
    """Menu and holds word lists"""
    # List of dictionaries - Topic: Everyday greetings
    everyday_greetings = [
        {"English" : "Hi", "Irish" : "Haigh"},
        {"English" : "Hello", "Irish" : "Dia Duit"},
        {"English" : "Bye", "Irish" : "Slán"},
        {"English" : "Please", "Irish" : "Le do thoil"},
        {"English" : "Thankyou", "Irish" : "Go raibh maith agat"},
        {"English" : "Welcome", "Irish" : "Fáilte"},
        {"English" : "Good Morning", "Irish" : "Maidin mhaith"}
        ]

    filler_words = [
        {"With" :"le"},
        {"And" :"agus"},
        {"Or" :"no"},
        {"The" :"an"}
        ]
    
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
        decision = int(input("\nEnter number option: "))

        if decision == 1:
            learn(everyday_greetings)

        elif decision == 2:
            vocabulary(everyday_greetings)

        elif decision == 3:
            profile()

        elif decision == 0:
            print("Session over.")
            break


if __name__ == "__main__":

    main()
